import urllib.request

URL = 'https://www.twitter.com'
PROXY_ADDRESS = "265.24.11.6:8080"
if __name__ == '__main__':
    resp = urllib.request.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})
print(f"Proxy server returns response headers: {resp.headers}")
