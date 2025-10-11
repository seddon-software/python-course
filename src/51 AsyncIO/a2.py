''' 
producer - consumer
'''
import asyncio
import random
import time

NUMBER_OF_CONSUMERS = 6

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue, NUMBER_OF_CONSUMERS),
        *(consumer(queue) for n in range(NUMBER_OF_CONSUMERS)),
    )

async def producer(queue, numberOfConsumers):
    async def generate_data():
        await asyncio.sleep(2)
        print(f"Producer")
        for message in list("ABCDEFGHIJKLMNOPQ\n"):
            await queue.put(message)

    await asyncio.gather(*(generate_data() for _ in range(numberOfConsumers)))
    # Sentinels for consumers to terminate
    [await queue.put(None) for _ in range(numberOfConsumers)]  
    
async def consumer(queue):
    while True:
        response = await queue.get()
        print(response, end="")
        await asyncio.sleep(2)
#        response = await queue.get()
        if response is None:
            print("consumer exiting")
            break

if __name__ == "__main__":
    asyncio.run(main())
