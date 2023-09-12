'''
In a asyncio application all the code runs in a single thread.  As we have seen this allows coroutines
to run concurrently, but it does not provide any performance gains for CPU intensive applications (use 
multi-processing for that).

However for IO bound asyncio applications there will be a lot of time spent waiting for IO to complete.  
In this case you can make performance gains by running tasks concurrently.  This is particularly evident 
when downloading from the web.

In this example we download data from a number of websites in parallel using the "aiohttp" library.  This 
library has been especially designed to allow asynchronous downloads.  We then compare our results with that 
obtained with the "requests" library (which performs the downloads synchronously).
'''

import asyncio
import timeit
import aiohttp
import requests

N = 5
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

def doAsynchronous():
    doAsynchronous.bytesRead = asyncio.run(main())

def doSynchronous():
    bytesRead = 0
    for _ in range(N):
        for site in sites:
            response = requests.get(f"http://{site}", headers={'Cache-Control': 'no-cache'})
            # print(f"{site}: {len(response.content)}")
            bytesRead += len(response.content)
    doSynchronous.bytesRead = bytesRead

print("comparing asynchronous and synchronous")

def timeDownloads(fn, lib, type):
    # to import fn with timeit we must make it global 
    global f
    f = fn
    print(f"{N:8} x {len(sites)} {type} downloads with {lib}", end=": ")
    secs = timeit.timeit(setup="from __main__ import f", stmt="f()", number=1)
    print(f"{f.bytesRead/2**20:6.2f} MB read in {secs:5.2f} secs")

timeDownloads(doAsynchronous, "aiohttp", "asynchronous")
timeDownloads(doSynchronous, "requests", "synchronous")


