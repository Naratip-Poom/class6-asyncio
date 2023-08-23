import asyncio
import time

async def print_after (message, delay):
    """print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    #use asyncio.gather to run two corotines concurrently
    await asyncio.gather(
        print_after("world!", 2)
        ,print_after("Hello", 1)
    )

asyncio.run(main())