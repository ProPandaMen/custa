from pathlib import Path
from custa.parser import parse_mks
from custa.renderer import render

import typer


CONTENT_DIR = Path("content")
OUTPUT_DIR = Path("output")
TEMPLATE_PATH = Path("custa/templates/layout.html")

def build():
    """Build .kms files into static HTML pages."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    for kms_file in CONTENT_DIR.glob("*.kms"):
        raw = kms_file.read_text(encoding="utf-8")
        nodes = parse_mks(raw)
        content_html = render(nodes)

        title = next(
            (n.props["value"] for n in nodes if n.type == "meta" and n.props.get("key") == "title"),
            kms_file.stem
        )

        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        html = template.format(title=title, content=content_html)

        output_path = OUTPUT_DIR / f"{kms_file.stem}.html"
        output_path.write_text(html, encoding="utf-8")

        typer.echo(f"✔ Built: {output_path}")
