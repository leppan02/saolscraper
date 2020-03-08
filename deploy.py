import requests
from pyquery import PyQuery as pq
import urllib
import re
import urllib.parse
import time
alphabet = "abcdefghijklmnopqrstuvwxyzåäö-"

def send(b):
    global words
    URL = "http://213.64.176.135:8000"
    words = ';'.join(words)
    data = {b : words} 
    r = requests.post(url = URL, data = data) 
    return

def new():
    URL = "http://213.64.176.135:8000"
    r = urllib.parse.unquote(requests.get(url = URL).content.decode())[:2]
    return r 
words = []
def rec(prefix):
    global words
    #print("Prefix:", prefix)
    res = requests.get("https://svenska.se/tri/f_saol.php?sok="+prefix+"%2A",
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
        return

    if res.text.find("...") != -1:
        for newLetter in range(29):
            rec(prefix+alphabet[newLetter])
        return

    #print(res.text)

    d = pq(res.text)
    for row in d(".slank"):
        word = d(row).html()
        word = word[word.find("</span>")+7:]
        word = word[:word.find("<span")]
        #print(word)
        words.append(word)

cur = new()
while(cur!='..'):
    starttime = time.time()
    print(cur)
    rec(cur)
    send(cur)
    print(cur+' done!!!')
    print('rate '+str(len(words)/(time.time()-starttime))+' words per second')
    words = []
    cur = new()
