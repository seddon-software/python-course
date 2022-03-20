'''
Futures
=======
A slightly different programming paradigm uses "futures".  In this example we use "asyncio.gather()" to collect
the results from a number of operations.  The operations are all started concurrently and "asyncio.gather()"
waits until all the calculations are finished before returning.  We can the examine the results with:
            for response in responses:
                print(response)

Behind the scenes, "asyncio.gather" uses "future" objects to run and store the results of these calculations.
In our next example, we will perform the same calculations, but use these "future" objects explicitly.
'''

import asyncio
import aiohttp

sites = "abc.com", "bbc.co.uk", "ibm.co.uk", "www.nytimes.com", "www.freeview.co.uk"

async def download(site):
    bytesRead = 0
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as response:
            html = await response.text()
            bytesRead += len(html)
            message = f"{site} returned {bytesRead//2**10}K characters"
            return message


async def main():
    # note each download yields immediately so that other downloads 
    # can run in parallel.  main waits until all results are available
    responses = await asyncio.gather(
        download(f"http://{sites[0]}"),
        download(f"http://{sites[1]}"),
        download(f"http://{sites[2]}"),
        download(f"http://{sites[3]}"),
        download(f"http://{sites[4]}")
    )
    for response in responses:
        print(response)
    
asyncio.run(main())

