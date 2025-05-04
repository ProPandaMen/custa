import http.server
import socketserver
import os
import typer

def serve(port: int = 8000):
    """Serve the output folder locally."""
    os.chdir("output")
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        typer.echo(f"🌐 Serving at http://localhost:{port}")
        httpd.serve_forever()
