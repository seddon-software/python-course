from requests_html import AsyncHTMLSession
import re, asyncio


async def get_quote(symbol):
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    asession = AsyncHTMLSession()
    r = await asession.get(url)
    await r.html.arender(timeout=50)
    pattern = r'<span.*data-field="MID_PRICE"  data-flash="true">(.*)</span>'
    m = re.search(pattern, r.text)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)
    await asession.close()

async def main():
    response = await asyncio.gather(
        get_quote("IBM"),
        get_quote("MSFT"),
        get_quote("BA.")
    )

asyncio.run(main())
