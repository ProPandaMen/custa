from pathlib import Path

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

    for kms_path in CONTENT_DIR.glob("*.kms"):
        page_html = render_page(kms_path, template, style_tags)
        output_file = OUTPUT_DIR / f"{kms_path.stem}.html"
        output_file.write_text(page_html, encoding="utf-8")
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


def render_page(kms_path: Path, template: str, style_tags: str) -> str:
    raw_content = kms_path.read_text(encoding="utf-8")
    nodes = parse_mks(raw_content)

    blocks = {}
    for node in nodes:
        if node.type == "meta" and node.props.get("key") == "title":
            blocks["title"] = node.props["value"]
        else:
            html = render([node])
            blocks.setdefault(node.type, "")
            blocks[node.type] += html

    if "title" not in blocks:
        blocks["title"] = kms_path.stem

    blocks["style"] = style_tags

    required_keys = {"title", "style", "main", "sidebar", "meta", "nav_bar", "footer"}
    for key in required_keys:
        blocks.setdefault(key, "")

    return template.format(**blocks)
