import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
      #MyHandler is a user-defined class that inherits from 
      # http.server.SimpleHTTPRequestHandler. This class 
      # allows you to customize how the server handles HTTP requests.  
    # Define a custom GET request handler method
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
                
#In the line of code self.wfile.write(b'404 - Not Found'), the b before the 
# string '404 - Not Found' indicates that the string is a bytes literal in Python.
# In Python, strings can be represented in two main ways: as text strings 
# (str) or as bytes strings (bytes). The b prefix is used to denote a bytes literal. Bytes literals are sequences of bytes, where each byte is represented as an integer value in the range 0-255.
# In the specific case of the self.wfile.write() method, it expects a 
# bytes-like object to be written to the output stream. 
# By using b'404 - Not Found', you are providing a bytes string, indicating 
# that the content should be written as raw binary data to the output stream. 
# This is common when writing binary data, such as file contents or HTTP response
#  bodies, to an output stream. For HTTP responses, it's essential to 
# specify the content as bytes because HTTP responses are binary data,
#  and the Content-Type header often determines how the data should be 
# interpreted by the client (e.g., as text, JSON, or binary data). By using bytes 
# literals, you ensure that the data is sent as-is without any text encoding applied.