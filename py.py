import requests
import urllib.request

def download():
    url = 'https://charasheet.vampire-blood.net/m42f60db264c78dec45cf046893d998df.js'
    title = 'src/malmal.json'
    return urllib.request.urlretrieve(url, title) 

a = download()
print(a)
