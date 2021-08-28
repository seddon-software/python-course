from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()
import re


async def get_quote(symbol, r):
    # url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    # session = AsyncHTMLSession()
    # r = await session.get(url)
    await r.html.arender(timeout=50)
    pattern = r'<span.*data-field="MID_PRICE"  data-flash="true">(.*)</span>'
    m = re.search(pattern, r.text)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)


async def get_1():
    symbol = get_1.symbol
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    r = await asession.get(url)
    await get_quote(symbol, r)
async def get_2():
    symbol = get_2.symbol
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    r = await asession.get(url)
    await get_quote(symbol, r)

async def get_3():
    symbol = get_3.symbol
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    r = await asession.get(url)
    await get_quote(symbol, r)

get_1.symbol = "IBM"
get_2.symbol = "MSFT"
get_3.symbol = "BA."
asession.run(get_1, get_2, get_3)
