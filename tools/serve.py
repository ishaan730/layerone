"""Local preview with the same URLs as production: /work/cars24-lego serves work/cars24-lego.html,
/experience serves experience.html, unknown paths get 404.html. Run: python3 tools/serve.py [port], default 8765."""
import http.server, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REDIRECTS = {"/clients": "/experience", "/blog": "/writing", "/services": "/pricing", "/index": "/"}


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_GET(self):
        path, _, q = self.path.partition("?")
        bare = path[:-5] if path.endswith(".html") else path
        if bare in REDIRECTS or (path.endswith(".html") and not path.startswith("/tools/")):
            self.send_response(308); self.send_header("Location", REDIRECTS.get(bare, bare if bare != "/index" else "/")); self.end_headers(); return
        if path != "/" and not os.path.splitext(path)[1] and os.path.isfile(os.path.join(ROOT, path.lstrip("/") + ".html")):
            self.path = path + ".html" + ("?" + q if q else "")
        elif not os.path.exists(os.path.join(ROOT, path.lstrip("/"))):
            self.path = "/404.html"
            body = open(os.path.join(ROOT, "404.html"), "rb").read()
            self.send_response(404); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body); return
        return super().do_GET()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"Layer One on http://localhost:{port}")
    http.server.ThreadingHTTPServer(("", port), H).serve_forever()
