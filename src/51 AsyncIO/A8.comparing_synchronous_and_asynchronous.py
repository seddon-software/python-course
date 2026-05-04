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
import aiohttp
import httpx
import time

sites = ["abc.com", "ibm.co.uk", "bbc.co.uk", "www.freeview.co.uk", "www.ietf.org"]

async def time_asynchronous(sites):
    async def fetch(session, url):
        async with session.get(url) as response:
            data = await response.read()
            return len(data)

    start = time.perf_counter()

    # Send the responses without compression in a most 30 seconds.
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=30), 
                                     headers={"Accept-Encoding": "identity"}) as session:
        tasks = [fetch(session, f"https://{site}") for site in sites]
        results = await asyncio.gather(*tasks)
        bytesRead = sum(results)

    end = time.perf_counter()
    print(f"{'asynchronous':14s}: {bytesRead} bytes read in {end - start:.2f}s")


def time_synchronous(sites):
    start = time.perf_counter()
    bytesRead = 0

    with httpx.Client(headers={"Accept-Encoding": "identity"}, follow_redirects=True, timeout=30.0) as client:
        for site in sites:
            response = client.get(f"https://{site}")
            bytesRead += len(response.content)
    end = time.perf_counter()
    print(f"{'synchronous':14s}: {bytesRead} bytes read in {end - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(time_asynchronous(sites))
    time_synchronous(sites)




