import requests
from pyquery import PyQuery as pq
import urllib
import re
import urllib.parse
import time
import pickle
alphabet = "abcdefghijklmnopqrstuvwxyzåäö-"

def send(b, words):
    URL = "http://213.64.176.135:8000"
    words = ';'.join(words)+'@'+b
    data = {'a' : words} 
    r = requests.post(url = URL, data = data) 
    return

def new():
    URL = "http://213.64.176.135:8000"
    tmp = urllib.parse.unquote(requests.get(url = URL).content.decode()).split('@')
    tmp[0] = tmp[0].split(';')
    return tmp

def exist(cur):
    #print("Prefix:", prefix)
    res =requests.get("https://svenska.se/tri/f_saol.php?sok="+cur,
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
while(inp[0]!='.'):
    words = []
    print(inp)
    for i in inp[0]:
        if(exist(i)):
            print(i)
            words.append(i)
    send(inp[1],words)
    inp = new()
