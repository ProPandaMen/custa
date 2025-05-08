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


def build():
    """Build .kms files into static HTML pages based on theme and layout configuration."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    config = load_config()
    theme = config["site"].get("theme", "default")
    template = load_template(config, theme)
    style_tags = copy_styles(config, theme)

    pages = config.get("pages", {})
    for url_path, page_data in pages.items():
        if isinstance(page_data, str):
            filename = page_data
            page_title = Path(page_data).stem
        else:
            filename = page_data["file"]
            page_title = page_data.get("title", Path(filename).stem)

        kms_path = CONTENT_DIR / filename
        if not kms_path.exists():
            typer.secho(f"⚠ File not found: {filename}", fg=typer.colors.YELLOW)
            continue

        html = render_page(kms_path, template, style_tags, page_title)

        if url_path == "/":
            output_file = OUTPUT_DIR / "index.html"
        else:
            target = OUTPUT_DIR / url_path.lstrip("/")
            target.parent.mkdir(parents=True, exist_ok=True)
            output_file = target.with_suffix(".html")

        output_file.write_text(html, encoding="utf-8")
        typer.echo(f"✔ Built: {output_file}")


def load_config() -> dict:
    return yaml.safe_load(CONFIG_FILE.read_text(encoding="utf-8"))


def load_template(config: dict, theme: str) -> str:
    template_dir = Path(config["layout"]["template_dir"].format(theme=theme))
    template_file = template_dir / "base.html"
    if not template_file.exists():
        raise FileNotFoundError(f"Template file not found: {template_file}")
    return template_file.read_text(encoding="utf-8")


def copy_styles(config: dict, theme: str) -> str:
    src_dir = Path(config["layout"]["stylesheet_dir"].format(theme=theme))
    dst_dir = OUTPUT_DIR / "static"

    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)

    style_tags = ""
    for css_file in dst_dir.glob("*.css"):
        rel_path = css_file.relative_to(OUTPUT_DIR)
        style_tags += f'<link rel="stylesheet" href="{rel_path.as_posix()}">\n'

    return style_tags


def render_page(kms_path: Path, template: str, style_tags: str, title: str) -> str:
    raw_content = kms_path.read_text(encoding="utf-8")
    nodes = parse_mks(raw_content)

    title = kms_path.stem
    blocks = defaultdict(str)

    for node in nodes:
        if node.type == "meta" and node.props.get("key") == "title":
            title = node.props["value"]
        elif node.type == "nav_bar":
            blocks["nav_bar"] += render([node])
        else:
            blocks["main"] += render([node])

    return template.format(
        title=title,
        style=style_tags,
        nav_bar=blocks["nav_bar"],
        main=blocks["main"],
    )
