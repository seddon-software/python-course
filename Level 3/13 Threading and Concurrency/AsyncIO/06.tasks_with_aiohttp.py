import asyncio
import time
import aiohttp


async def download(site):
    for _ in range(25):
        print(f"downloading {site}")
        async with aiohttp.ClientSession() as session:
            async with session.get(site) as response:
                # print("Status:", response.status)
                # print("Content-type:", response.headers['content-type'])

                html = await response.text()
#                print("Body:", html[:15], "...")
        # note aiohttp is asynchronous.
#        await asyncio.sleep(0)      # standard way to yield to event loop

async def main():
    # schedule downloads to be run in parallel
    task1 = asyncio.create_task(download("http://abc.com"))
    task2 = asyncio.create_task(download("http://bbc.co.uk"))
    task3 = asyncio.create_task(download("http://ibm.co.uk"))

    await task1
    await task2
    await task3

asyncio.run(main())

