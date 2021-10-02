import re
from requests_html import HTMLSession


# Note: the first time you run this program it will download the Chrome driver
def get_quote(symbol):
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    pattern = r'<span.*data-field="MID_PRICE"  data-flash="true">(.*)</span>'
    m = re.search(pattern, r.text)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)
    

print("London Stock Exchange Quotes")
get_quote("IBM")
get_quote("HL.")
get_quote("BA.")
get_quote("XX")
get_quote("MSFT")
get_quote("BATS")






