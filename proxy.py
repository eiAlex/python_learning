import requests

proxies = {
    "https":"49.128.186.165:8080",
    "http":"49.128.186.165:8080"
}

url = "http://api.ipify.org?format=json"

r = requests.get(url,proxies=proxies)

print(r.json())