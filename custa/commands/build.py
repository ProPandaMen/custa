from pathlib import Path
from collections import defaultdict

from custa.parser import parse_mks
from custa.renderer import render

import typer
import yaml
import shutil

CONTENT_DIR = Path("content")
OUTPUT_DIR = Path("output")
CONFIG_FILE = Path("custa.config.yaml")


def build(debug: bool = False):
    """Build .cst files into static HTML pages based on theme and layout configuration."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    config = load_config()
    theme = config["site"].get("theme", "default")
    template = load_template(config, theme)
    style_tags = copy_files(config, theme)

    generated_filenames = set()

    pages = config.get("pages", {})
    for url_path, page_data in pages.items():
        output_file, filename = build_page_from_route(url_path, page_data, template, style_tags, debug)
        if output_file:
            generated_filenames.add(filename)

    build_fallback_pages(generated_filenames, template, style_tags, debug)


def load_config() -> dict:
    return yaml.safe_load(CONFIG_FILE.read_text(encoding="utf-8"))


def load_template(config: dict, theme: str) -> str:
    template_dir = Path(config["layout"]["template_dir"].format(theme=theme))
    template_file = template_dir / "base.html"
    if not template_file.exists():
        raise FileNotFoundError(f"Template file not found: {template_file}")
    return template_file.read_text(encoding="utf-8")


def copy_files(config: dict, theme: str) -> str:
    src_dir = Path(config["layout"]["stylesheet_dir"].format(theme=theme))
    img_dir = Path(config["layout"]["image_dir"].format(theme=theme))
    dst_dir = OUTPUT_DIR / "static"

    if dst_dir.exists():
        shutil.rmtree(dst_dir)

    shutil.copytree(src_dir, dst_dir)
    shutil.copytree(img_dir, dst_dir, dirs_exist_ok=True)

    style_tags = ""
    for css_file in dst_dir.glob("*.css"):
        rel_path = css_file.relative_to(OUTPUT_DIR)
        style_tags += f'<link rel="stylesheet" href="{rel_path.as_posix()}">\n'

    return style_tags


def render_page(nodes, template: str, style_tags: str, title: str) -> str:
    blocks = defaultdict(str)

    for node in nodes:
        if node.type == "meta" and node.props.get("key") == "title":
            title = node.props["value"]
        elif node.type == "navbar":
            blocks["navbar"] += render([node])
        else:
            blocks["main"] += render([node])

    return template.format(
        title=title,
        style=style_tags,
        navbar=blocks["navbar"],
        main=blocks["main"],
    )


def print_tree(node, indent=0):
    typer.echo("  " * indent + node.type)
    for child in node.children:
        print_tree(child, indent + 1)


def build_page_from_route(url_path, page_data, template, style_tags, debug):
    if isinstance(page_data, str):
        filename = page_data
        page_title = Path(page_data).stem
    else:
        filename = page_data["file"]
        page_title = page_data.get("title", Path(filename).stem)

    cst_path = CONTENT_DIR / filename
    if not cst_path.exists():
        typer.secho(f"⚠ File not found: {filename}", fg=typer.colors.YELLOW)
        return None, filename

    raw_content = cst_path.read_text(encoding="utf-8")
    nodes = parse_mks(raw_content)

    if debug:
        typer.echo(f"📄 Debug structure for {filename}:")
        for node in nodes:
            print_tree(node)
        print("=" * 40)

    html = render_page(nodes, template, style_tags, page_title)

    if url_path == "/":
        output_file = OUTPUT_DIR / "index.html"
    else:
        target = OUTPUT_DIR / url_path.lstrip("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        output_file = target.with_suffix(".html")

    output_file.write_text(html, encoding="utf-8")
    typer.echo(f"✔ Built: {output_file}")

    return output_file, filename


def build_fallback_pages(generated_filenames, template, style_tags, debug):
    for cst_path in CONTENT_DIR.glob("*.cst"):
        if cst_path.name in generated_filenames:
            continue

        stem = cst_path.stem
        raw_content = cst_path.read_text(encoding="utf-8")
        nodes = parse_mks(raw_content)

        if debug:
            typer.echo(f"📄 Debug structure for {cst_path.name}:")
            for node in nodes:
                print_tree(node)
            print("=" * 40)

        html = render_page(nodes, template, style_tags, stem)
        output_file = OUTPUT_DIR / f"{stem}.html"
        output_file.write_text(html, encoding="utf-8")
        typer.echo(f"✔ Built: {output_file} (fallback)")
