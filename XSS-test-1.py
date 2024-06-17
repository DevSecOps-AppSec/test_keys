import http.server
import urllib.parse

comments = []

class XSSHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <html>
                    <body>
                        <h1>Comments</h1>
                        <form action="/comment" method="post">
                            <input type="text" name="comment">
                            <input type="submit" value="Add Comment">
                        </form>
                        <h2>All Comments</h2>
                        <ul>
            """)
            for comment in comments:
                self.wfile.write(f"<li>{comment}</li>".encode())
            self.wfile.write(b"""
                        </ul>
                    </body>
                </html>
            """)

    def do_POST(self):
        if self.path == '/comment':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            comment = urllib.parse.parse_qs(post_data.decode())['comment'][0]
            comments.append(comment)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

if __name__ == '__main__':
    server = http.server.HTTPServer(('localhost', 8080), XSSHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()
