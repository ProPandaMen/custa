from custa.commands import init, build, serve

import typer

app = typer.Typer()

app.command()(init.init)
app.command()(build.build)
app.command()(serve.serve)

if __name__ == "__main__":
    app()
