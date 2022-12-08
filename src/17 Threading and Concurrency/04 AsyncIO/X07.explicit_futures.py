'''
Explicit Futures
================
As promised, this is the same example, but with the "future" objects exposed to our code.  The code looks
slightly more complicated this time, mainly because I've allowed "asyncio.gather" to take a variable number
of parameters.

The problem with doing this is that all the parameters to "asyncio.gather" are function calls and they can't 
easily be set up in advance because the call has to be made in the parameter list and not before.  We can
work around this restriction by creating a list of partial functions and then pass this list to "asyncio.gather"
in a list comprehension.  We do this because we can expand the comprehension with * and call each operation 
with ():
            *[op() for op in ops]
'''

from functools import partial
import asyncio
import aiohttp

sites = "abc.com", "bbc.co.uk", "ibm.co.uk", "www.nytimes.com", "www.freeview.co.uk"

async def download(site, future):
    bytesRead = 0
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as response:
            html = await response.text()
            bytesRead += len(html)
            message = f"{site} returned {bytesRead//2**10}K characters"
            future.set_result(message)

async def main():
    # note each download yields immediately so that other downloads 
    # can run in parallel.  main waits until all results are available
    event_loop = asyncio.get_event_loop()

    # create a future for each site
    futures = []
    for site in sites:
        futures.append( event_loop.create_future() )

    # create a list of partial functions to pass to asycio.gather
    ops = []
    for n,site in enumerate(sites):
        ops.append(partial(download, f"http://{sites[n]}", futures[n]))

    # gather takes a list of called functions, so need to use partial functions to ensure functions are
    # called as parameters to gather.  Expand the list comprehension with * and call each partial function.
    await asyncio.gather(*[op() for op in ops])

    # print out results contained in futures    
    for future in futures:
        print(future.result())
    
asyncio.run(main())

