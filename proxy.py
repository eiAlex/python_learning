import requests

proxies = {
    "https":"49.128.186.165:8080",
    "http":"49.128.186.165:8080"
}

url = "http://www.americanas.com.br/"
while True:
    
    r = requests.get(url)

    print(r)