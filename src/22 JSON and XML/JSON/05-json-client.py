import urllib.request
from urllib.error import HTTPError 
import json

# send a request to the server with a query string
# the server will add 100 to each parameter and return the result as JSON


def send_data(url):
    try:
        jsonAsBytes = urllib.request.urlopen(url).read()
    except HTTPError as e:
        print(e)
        return
    # response comes back as bytes, but must be converted to JSON
    jsonResponse = jsonAsBytes.decode("UTF-8")
    # convert JSON to a Python dictionary
    pythonDictionary = json.loads(jsonResponse)
    print(type(pythonDictionary))
    print(pythonDictionary)

url = "http://localhost:8002/anything?x=1&y=2&z=3&x=4&y=7&x=3"
send_data(url)

url = "http://localhost:8002/anything?red=106&green=204&blue=34"
send_data(url)

url = "http://localhost:8002/anything?junk=xx"
send_data(url)


