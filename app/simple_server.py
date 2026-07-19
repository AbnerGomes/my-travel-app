import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in {"/", "/health"}:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            payload = {"status": "ok", "message": "Travel App backend is running"}
            if self.path == "/":
                payload["route"] = "root"
            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        if self.path == "/search/flights":
            content_length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(content_length).decode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "origin": "GRU",
                "destination": "GIG",
                "results": [{"airline": "Example Air", "price": 520.0, "currency": "BRL", "duration_hours": 4.5, "stops": 0}]
            }).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), Handler)
    print("Server running on http://127.0.0.1:8000")
    server.serve_forever()
