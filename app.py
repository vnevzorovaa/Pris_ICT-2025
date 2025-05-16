from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from my app!")

if __name__ == "__main__":
    server = HTTPServer(("", 8080), MyHandler)
    print("Starting server on port 8080")
    server.serve_forever()
