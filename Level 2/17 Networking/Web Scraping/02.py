import asyncio
from requests_html import AsyncHTMLSession

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


asession = AsyncHTMLSession()

async def get_it(symbol):
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    r = await asession.get(url)
    await get_quote(symbol, r)

async def main():
#    asession.run(get_it("IBM"), get_it("MSFT"), get_it("BA."))
    await get_it("IBM")
    await get_it("MSFT")
    await get_it("BA.")

asyncio.run(main())
