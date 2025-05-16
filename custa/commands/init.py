from pathlib import Path
import shutil
import typer

def init(force: bool = False):
    """Initializes the Custa project structure."""
    src = Path(__file__).parent.parent / "project_template"
    dst = Path.cwd()
    
    if not force and any((dst / f).exists() for f in ["content", "themes", "custa.config.yaml"]):
        typer.echo("⚠️ Project is already initialized or some folders already exist.")
        raise typer.Exit(1)
    
    shutil.copytree(src, dst, dirs_exist_ok=True)
    typer.echo("✅ Custa project has been successfully initialized.")
