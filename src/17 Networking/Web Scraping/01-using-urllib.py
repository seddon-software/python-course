import urllib.request
import re

def get_quote2(symbol):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    
    url = "http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
    url = f'https://finance.google.com/finance?q={symbol}'
    headers={'User-Agent':user_agent,} 
    
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    content = data.decode("UTF-8")
    print(content)
    
def get_quote(symbol):
    base_url = 'https://finance.google.com/finance?q='
    content = urllib.request.urlopen(base_url + symbol).read()
    content = content.decode("UTF-8")
    pattern = r'class="pr"[^>]*>[^>]*>(.*)</span>'
    m = re.search(pattern, content)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)
        
get_quote2("IBM")
# get_quote("MS")
# get_quote("XX")
# get_quote("MSFT")
# get_quote("ERICB")


1



