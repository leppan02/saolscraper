from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from io import BytesIO
import urllib.parse
import socket 
import pickle
available = []
done = []
pending = []
alldata = []
def readvar():
    global available, done, pending, alldata
    with open('all.data', 'rb') as filehandle:
        alldata = pickle.load(filehandle)
    with open('available.data', 'rb') as filehandle:
        available = pickle.load(filehandle)

    with open('pending.data', 'rb') as filehandle:
        pending = pickle.load(filehandle)

    with open('done.data', 'rb') as filehandle:
        done = pickle.load(filehandle)


def writevar():
    global available, done, pending
    with open('available.data', 'wb') as filehandle:
        pickle.dump(available, filehandle)

    with open('pending.data', 'wb') as filehandle:
        pickle.dump(pending, filehandle)

    with open('done.data', 'wb') as filehandle:
        pickle.dump(done, filehandle)

def add(a):
    a = a.split('@')[0].split(';')
    print(a)
    f = open("ndict.txt", "a")
    for word in a:
        f.write(word + "\n")
    f.close()

def seen(a):
    a = a.split('@')[1]
    if(int(a) in pending):
        pending.remove(int(a))
        done.append(int(a))
        return True
    return False

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(currentletter().encode())
        writevar()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        body = self.rfile.read(content_length)
        body = urllib.parse.unquote((body.decode('UTF-8')))[2:]
        if(seen(body)):
            add(body)
        writevar()

def currentletter():
    if(len(available) == 0):
        if(len(pending) == 0):
            return '.'
        u = pending[0]
        pending.remove(u)
        pending.append(u)
        return alldata[u]+'@'+str(u)
    ut = available[0]
    available.remove(ut)
    pending.append(ut)
    return alldata[ut]+'@'+str(ut)

    
    
readvar()
httpd = HTTPServer((socket.gethostbyname(socket.gethostname()),8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
