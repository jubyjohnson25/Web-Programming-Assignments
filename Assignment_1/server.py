import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
     
    def do_GET(self):
            if self.path =='/home.html':
                self.send_response(301)
                self.send_header('Location', 'http://www.google.com')
                self.end_headers()
            elif self.path =='/student.html':
                 self.send_response(200)
                 self.send_header('Content-type','text/html' )
                 self.end_headers()
                 with open('student.html', 'rb') as file:
                      self.wfile.write(file.read())
            else:
                  self.send_response(404)
                  self.send_header('Content-type','text/html' )
                  self.end_headers()
                  self.wfile.write(b'404 - Not found!')
                 
with socketserver.TCPServer(("", PORT), MyHandler) as httpd: #The server listens on the specified IP address ("", meaning all available network interfaces) and port (PORT
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
                
