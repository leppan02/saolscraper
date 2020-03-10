import requests
from pyquery import PyQuery as pq
import urllib
import re
import urllib.parse
import time
import pickle
alphabet = "abcdefghijklmnopqrstuvwxyzåäö-"

def send(b):
    URL = "http://213.64.176.135:8000"
    words = ';'.join(words)
    data = {b : words} 
    r = requests.post(url = URL, data = data) 
    return

def new():
    URL = "http://213.64.176.135:8000"
    return = urllib.parse.unquote(requests.get(url = URL).content.decode())[:2].split(';')

def exist(cur):
    #print("Prefix:", prefix)
    res = requests.get("https://svenska.se/tri/f_saol.php?sok="+cur,
        headers={
            'Host': 'svenska.se',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'https://svenska.se/tre/?sok=ab*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,da;q=0.5,nb;q=0.4'
        })

    if res.text.find("gav inga svar") != -1:
        return False
    return True

inp = new()
while(inp!='.'):
    words = []
    for i in inp:
        if(test(i.decode('ascii'))):
            words.append(i)
    send(words)
    inp = new()
