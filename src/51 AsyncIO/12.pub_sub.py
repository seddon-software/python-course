''' 
producer - consumer
'''

import os, time
import asyncio, aiohttp

os.system("fuser -k 8000/tcp")  # kill previous incarnations
os.system("flask --app server run --host localhost --port 8000 &")
time.sleep(2)                   # wait for the server to start

NUMBER_OF_SUBSCRIBERS = 10
count = NUMBER_OF_SUBSCRIBERS

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
                    if count == 0: break


    await asyncio.gather(*(generate_data() for _ in range(numberOfConsumers)))
    
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
