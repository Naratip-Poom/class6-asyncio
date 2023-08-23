import asyncio
import time

async def example (message):
    print(f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of :", message)
   

async def main():
    #start corotine twice (hopefully they start!)
    first_awaitable = example("first call ")
    second_awaitable = example("scound call ")
    #wait for corotine to finish
    await second_awaitable
    await first_awaitable
    # await second_awaitable

asyncio.run(main())