import re, sys
import asyncio
from requests_html import AsyncHTMLSession
import pyppeteer.launcher as l
import pyppeteer

# Note: the first time you run this program it will download the Chrome driver
async def get_quote(symbol):
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    session = AsyncHTMLSession()
    r = await session.get(url)
    await r.html.arender(timeout=50)
    pattern = r'<span.*data-field="MID_PRICE"  data-flash="true">(.*)</span>'
    m = re.search(pattern, r.text)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)
    await session.close()

async def main():
    print("London Stock Exchange Quotes")
    response = await asyncio.gather(
        get_quote("IBM"),
        get_quote("HL."),
        get_quote("BA."),
        get_quote("XX"),
        get_quote("MSFT"),
        get_quote("BATS")
    )

asyncio.run(main())




