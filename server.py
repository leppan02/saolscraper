from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from io import BytesIO
import urllib.parse
import socket 

def add(a):
    f = open("dict.txt", "a")
    for word in a:
        f.write(word + "\n")
    f.close()
def seen(a):
    f = open("seen.txt", "a")
    f.write(a + "\n")
    f.close()
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(currentletter().encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        body = self.rfile.read(content_length)
        body = urllib.parse.unquote((body.decode('UTF-8')))
        seen(body[0])
        add(body[2:].split(';'))
alphabet = "abcdefghijklmnopqrstuvwxyzåäö."
start = -1
def currentletter():
    global start
    start = min(start+1,len(alphabet)-1)
    return alphabet[start]
    

httpd = HTTPServer((socket.gethostbyname(socket.gethostname()),8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
