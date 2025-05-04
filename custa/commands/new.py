from pathlib import Path

import typer


CONTENT_DIR = Path("content")

def new(filename: str):
    """Create a new .kms file in the content directory."""
    path = CONTENT_DIR / filename
    if not path.suffix:
        path = path.with_suffix(".kms")

    if path.exists():
        typer.echo("⚠️ File already exists!")
        raise typer.Exit()

    with open(path, "w", encoding="utf-8") as f:
        f.write("#title: New Page\n\n@section\nWelcome to Custa!")

    typer.echo(f"✅ Created: {path}")
