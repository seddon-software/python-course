import asyncio
import time
import requests

    
async def download(site):
    for _ in range(5):
        print(f"downloading {site}")
        # note requests is not asynchronous.  This means the following
        # line blocks until complete
        requests.get(site)
        await asyncio.sleep(0)      # standard way to yield to event loop

async def main():
    # schedule downloads to be run in parallel
    task1 = asyncio.create_task(download("http://abc.com"))
    task2 = asyncio.create_task(download("http://bbc.co.uk"))
    task3 = asyncio.create_task(download("http://ibm.co.uk"))

    await task1
    await task2
    await task3

asyncio.run(main())

