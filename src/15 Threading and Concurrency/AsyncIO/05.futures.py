import asyncio
import requests

async def download(site):
    # download 5 times to slow program down
    for _ in range(5):
        await asyncio.sleep(0)      # standard way to yield to event loop
        print(f"downloading from {site}")
        response = requests.get(site)
    message = f"{site} returned {len(response.text)} characters"
    return message


async def main():
    # note each download yields immediately so that other downloads 
    # can run in parallel.  main waits until all results are available
    response = await asyncio.gather(
        download("http://ibm.com"),
        download("http://bbc.co.uk"),
        download("http://abc.com")
    )
    print(response)
    
asyncio.run(main())

