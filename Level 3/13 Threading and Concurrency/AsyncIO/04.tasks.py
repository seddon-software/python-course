import asyncio
import time
import requests

    
async def download(site):
    def get(n):
        for _ in range(5):
            print(f"downloading {site}")
            requests.get(site)
    get(5)
    await asyncio.sleep(0)      # standard way to yield to event loop
    get(5)

async def main():
    # schedule downloads to be run in parallel
    # note each download only yields after 5 downloads
    task1 = asyncio.create_task(download("http://abc.com"))
    task2 = asyncio.create_task(download("http://bbc.co.uk"))
    task3 = asyncio.create_task(download("http://ibm.co.uk"))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    await task3
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

