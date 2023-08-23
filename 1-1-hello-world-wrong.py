import asyncio
import time

async def print_after (message, delay):
    """print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    #start corotine twice (hopefully they start!)
    first_awaitable = print_after("world!",2)
    second_awaitable = print_after("HEllo!",1)
    #await first_awaitable
    await second_awaitable
    await first_awaitable
    # await second_awaitable

asyncio.run(main())
#ไม่ใช่โปรเเกรม ASY เพราะเมื่อไรที่เราเรียก coพotine มันเป็นฟังชัน ไม่ใช่ task
#ถ้าเปลี่ยน = ไม่ไช่ asy (hello, world)