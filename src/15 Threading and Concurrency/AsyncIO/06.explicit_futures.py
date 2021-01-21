import asyncio
import requests

# this example uses future objects.  Each download explicitly sets
# its result
async def download(site, future):
    # download 5 times to slow program down
    for _ in range(5):
        await asyncio.sleep(0)      # standard way to yield to event loop
        print(f"downloading from {site}")
        response = requests.get(site)
    message = f"{site} returned {len(response.text)} characters"
    future.set_result(message)

async def main():
    event_loop = asyncio.get_event_loop()
    f1 = event_loop.create_future()
    f2 = event_loop.create_future()
    f3 = event_loop.create_future()
    # wait until all futures results have been set
    await asyncio.gather(
        download("http://ibm.com", f1),
        download("http://bbc.co.uk", f2),
        download("http://abc.com", f3)
    )
    print(f1.result())
    print(f2.result())
    print(f3.result())
    
        
asyncio.run(main())


