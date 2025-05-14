from http.server import BaseHTTPRequestHandler, HTTPServer

from custa.parser import parse_kms_file
from custa.renderer import render

import os
import yaml


CONFIG_PATH = "custa.config.yaml"
CONTENT_DIR = "content"
OUTPUT_DIR = "output"
STATIC_PREFIX = "/static/"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

pages = config.get("pages", {})


class CustaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = self._clean_path(self.path)

        if route.startswith(STATIC_PREFIX):
            self._serve_static(route)
        else:
            self._serve_page(route)

    def _clean_path(self, path: str) -> str:
        route = path or "/"
        if "?" in route:
            route = route.split("?", 1)[0]
        return route

    def _serve_static(self, route: str):
        file_path = os.path.join(OUTPUT_DIR, route.lstrip("/"))
        if not os.path.exists(file_path):
            self.send_error(404, "Static file not found")
            return

        content_type = self._get_content_type(file_path)
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()
        with open(file_path, "rb") as f:
            self.wfile.write(f.read())

    def _serve_page(self, route: str):
        if route.endswith("/"):
            route = route[:-1] or "/"  # убираем лишний /
        page = pages.get(route)
        if not page:
            self.send_error(404, "Page not found")
            return

        output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(page['file'])[0]}.html")
        if not os.path.exists(output_path):
            self.send_error(404, f"Built page not found: {output_path}")
            return

        try:
            with open(output_path, "rb") as f:
                html_bytes = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html_bytes)))
            self.end_headers()
            self.wfile.write(html_bytes)
        except Exception as e:
            try:
                self.send_error(500, f"Failed to serve HTML: {e}")
            except BrokenPipeError:
                print("⚠️ Broken pipe while sending static HTML page")

    def _get_content_type(self, path: str) -> str:
        if path.endswith(".css"):
            return "text/css; charset=utf-8"
        if path.endswith(".js"):
            return "application/javascript"
        if path.endswith(".png"):
            return "image/png"
        if path.endswith(".jpg") or path.endswith(".jpeg"):
            return "image/jpeg"
        if path.endswith(".svg"):
            return "image/svg+xml"
        return "application/octet-stream"


def serve(port: int = 8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, CustaHandler)
    print(f"🚀 Server running at http://localhost:{port}")
    httpd.serve_forever()
