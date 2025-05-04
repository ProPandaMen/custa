from custa.commands import build, new, serve

import typer

app = typer.Typer()

app.command()(build.build)
app.command()(new.new)
app.command()(serve.serve)

if __name__ == "__main__":
    app()
