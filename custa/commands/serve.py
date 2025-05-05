import http.server
import socketserver
import os
import typer

def serve(port: int = 8000):
    """Serve the output folder locally."""
    os.chdir("output")
    handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            typer.echo(f"🌐 Serving at http://localhost:{port}")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48 or "Address already in use" in str(e):
            typer.secho(f"❌ Port {port} is already in use. Try a different one with --port.", fg=typer.colors.RED)
        else:
            raise
