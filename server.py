import http.server
import socketserver

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            # Set the response code
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Open and serve your custom 404.html file
            try:
                with open("404.html", "rb") as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.wfile.write(b"404 Not Found (Custom page missing)")
        else:
            super().send_error(code, message, explain)

PORT = 8000
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

