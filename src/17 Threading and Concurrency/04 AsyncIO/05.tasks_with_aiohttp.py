'''
Tasks with aiohttp
==================
In a CPU bound asyncio application all the code runs in a single thread.  As we have seen this allows coroutines
to run concurrently, but it does not provide any performance gains (use multi-processing for that).

However for IO bound asyncio applications there will be a lot of time spent waiting for IO to complete.  In this
case you can make performance gains by running tasks concurrently.  This is particularly evident when downloading
from the web.

In this example we download data from a number of websites in parallel using the "aiohttp" library.  This library
has been especially designed to allow asynchronous downloads.  We then compare our results with that obtained
with the "requests" library (which performs the downloads synchronously).
'''

import asyncio
import timeit
import aiohttp
import requests
N = 10

sites = "abc.com", "bbc.co.uk", "ibm.co.uk", "www.nytimes.com", "www.freeview.co.uk"
async def download(site):
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as response:
            html = await response.text()
            # print(f"{site}: {len(html)}")
            return len(html)

async def main():
    # schedule downloads to be run in parallel
    tasks = []
    for _ in range(N):
        for site in sites:
            tasks.append( asyncio.create_task(download(f"http://{site}")) )

    bytesRead = 0
    for task in tasks:
        bytesRead += await task
    return bytesRead

def doit():
    doit.bytesRead = asyncio.run(main())

def doit2():
    bytesRead = 0
    for _ in range(N):
        for site in sites:
            response = requests.get(f"http://{site}", headers={'Cache-Control': 'no-cache'})
            # print(f"{site}: {len(response.content)}")
            bytesRead += len(response.content)
    doit2.bytesRead = bytesRead

print("comparing asynchronous and synchronous")
print(f"\t{N} x {len(sites)} asynchronous downloads with aiohttp", end=": ")
secs = timeit.timeit(setup="from __main__ import doit", stmt="doit()", number=1)
print(f"{doit.bytesRead/2**20:6.2f}MB read in {secs:5.2f} secs")

print(f"\t{N} x {len(sites)} synchronous downloads with requests", end=": ")
secs = timeit.timeit(setup="from __main__ import doit2", stmt="doit2()", number=1)
print(f"{doit2.bytesRead/2**20:6.2f}MB read in {secs:5.2f} secs")

