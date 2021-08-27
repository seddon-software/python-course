import re
import asyncio
from requests_html import AsyncHTMLSession

# Note: the first time you run this program it will download the Chrome driver
async def get_quote(symbol):
    url = f'https://www.lse.co.uk/SharePrice.asp?shareprice={symbol}'
    session = AsyncHTMLSession()
    r = await session.get(url)
    await r.html.arender()
    pattern = r'<span.*data-field="MID_PRICE"  data-flash="true">(.*)</span>'
    m = re.search(pattern, r.text)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)

async def main():
    print("London Stock Exchange Quotes")
    task1 = asyncio.create_task(get_quote("IBM"))
    task2 = asyncio.create_task(get_quote("HL."))
    task3 = asyncio.create_task(get_quote("BA."))
    task4 = asyncio.create_task(get_quote("XX"))
    task5 = asyncio.create_task(get_quote("MSFT"))
    task6 = asyncio.create_task(get_quote("BATS"))
    await task1
    await task2
    await task3
    await task4
    await task5
    await task6

asyncio.run(main())





