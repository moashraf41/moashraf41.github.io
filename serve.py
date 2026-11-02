"""Local preview server for the portfolio.

Serves the folder as static files, gzipping text assets the way real hosting does
(GitHub Pages / Netlify / Vercel all compress by default). Use this instead of
`python -m http.server` so local numbers match production.

    python serve.py          # http://localhost:8000
    python serve.py 8080     # custom port
"""

import gzip
import io
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

COMPRESSIBLE = {
    "text/html",
    "text/css",
    "text/plain",
    "text/javascript",
    "application/javascript",
    "application/json",
    "image/svg+xml",
}


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".woff2": "font/woff2",
        ".webp": "image/webp",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        if self.path.startswith("/fonts/") or "?v=" in self.path:
            self.send_header("Cache-Control", "public, max-age=31536000, immutable")
        self.send_header("Vary", "Accept-Encoding")
        super().end_headers()

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            index = os.path.join(path, "index.html")
            if os.path.isfile(index):
                path = index
        if not os.path.isfile(path):
            return super().send_head()
        ctype = self.guess_type(path)
        accepts_gzip = "gzip" in self.headers.get("Accept-Encoding", "")
        if ctype not in COMPRESSIBLE or not accepts_gzip:
            return super().send_head()

        with open(path, "rb") as fh:
            body = gzip.compress(fh.read(), 6)
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Encoding", "gzip")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        return io.BytesIO(body)


if __name__ == "__main__":
    with ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving {ROOT} on http://localhost:{PORT}")
        httpd.serve_forever()
