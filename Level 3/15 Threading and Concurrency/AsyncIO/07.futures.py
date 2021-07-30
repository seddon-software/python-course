import asyncio
import aiohttp

async def download(visits, site):
    count = 0
    for _ in range(visits):
        print(f"downloading {site}")
        async with aiohttp.ClientSession() as session:
            async with session.get(site) as response:
                html = await response.text()
                count += len(html)
    message = f"{site} returned {count//1000}K characters"
    return message

async def main():
    # note each download yields immediately so that other downloads 
    # can run in parallel.  main waits until all results are available
    response = await asyncio.gather(
        download(15, "http://ibm.com"),
        download(20, "http://bbc.co.uk"),
        download(25, "http://abc.com")
    )
    print(response)
    
asyncio.run(main())

