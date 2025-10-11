'''  
This example illustrates the software pattern Pub/Sub (publish and subscribe).  The pattern 
has a publisher and a number of subscribers.  The publisher notifies interested parties when 
an event occurs using a callback (delivered via an async queue).  Typically all the 
subscribers register with the publisher so that it can callback to each subscriber.

The publisher gets a set of temperatures from an application server across the internet.  We 
simulate the server application with a Flask server running on the localhost, port 8000.

The publisher sends temperatures to the subscribers using the async queue.  Each subscriber 
announces when the temperature goes above a "max_temperature".  This "max_temperature" is
defined as the id of the subscriber plus 19.0C (chosen somewhat artificially).
'''

import os, time
import asyncio, aiohttp

def startFlaskServer():
    os.system("fuser -k 8000/tcp")  # kill previous incarnations
    os.system("flask --app server run --host localhost --port 8000 &")
    time.sleep(2)                   # wait for the server to start

startFlaskServer()
NUMBER_OF_SUBSCRIBERS = 10
count = NUMBER_OF_SUBSCRIBERS

# main fires off a publisher and several subscribers that communicate via an async queue
async def main():
    async def start():
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:8000/start') as response: pass
    await start()
    queue = asyncio.Queue()
    await asyncio.gather(
        publisher(queue, NUMBER_OF_SUBSCRIBERS),
        *(subscriber(id, queue) for id in range(NUMBER_OF_SUBSCRIBERS)),

    )

###################### Publisher #############################
async def publisher(queue, numberOfConsumers):
    async def generate_data():
        url = "http://localhost:8000/getTemperature"
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(url) as response:
                    temperature = await response.text()
                    try:
                        temperature = float(temperature)
                    except:
                        temperature = None    # no more data
                    await queue.put(temperature)
                    if not temperature: break
                    if count == 0: break        # all subscribers have exited
    await asyncio.gather(*(generate_data() for _ in range(numberOfConsumers)))

###################### Subscriber #############################
async def subscriber(id, queue):
    global count
    maxTemperature = 19.0 + id
    while True:
        response = await queue.get()
        if response:
            if response > maxTemperature:
                print(f"Subscriber {id} notes max temperature exceeded:{response:6.2f}")
                break # exiting because of max temperature
        else:
            break  # exiting because data exhausted
    count -= 1

if __name__ == "__main__":
    asyncio.run(main())
