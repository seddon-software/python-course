import asyncio
import aiohttp

async def download(visits, site, future):
    count = 0
    for _ in range(visits):
        print(f"downloading {site}")
        async with aiohttp.ClientSession() as session:
            async with session.get(site) as response:
                html = await response.text()
                count += len(html)
    message = f"{site} returned {count//1000}K characters"
    future.set_result(message)

async def main():
    event_loop = asyncio.get_event_loop()
    f1 = event_loop.create_future()
    f2 = event_loop.create_future()
    f3 = event_loop.create_future()

    # wait until all futures results have been set
    await asyncio.gather(
        download(15, "http://ibm.com", f1),
        download(20, "http://bbc.co.uk", f2),
        download(25, "http://abc.com", f3)
    )
    print(f1.result())
    print(f2.result())
    print(f3.result())
    
asyncio.run(main())

