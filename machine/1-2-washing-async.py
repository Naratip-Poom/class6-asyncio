"""
ต้องการซักผ้า 2 ตะกร้า แบบ asynchronous io
กระบวนการซักผ้า 1 ตะกร้า คือ
1. หยอดเหรียญเพื่อซักผ้า
2. นำผ้าเข้าเครื่องซักผ้า
3. ซักผ้าเสร็จ (ใช้เวลา 5 วินาที)

เนื่องจากมีเครื่องซักผ้าที่สามารถพร้อมใช้งานได้ 2 เครื่องพร้อมกัน 

เปลี่ยนการทำงานเป็นแบบ asynchronous io 
"""

import time

import asyncio

async def wash(basket):
    print(f'{time.ctime()} - Washing Machine ({basket}): Put the coin')
    print(f'{time.ctime()} - Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'{time.ctime()} - Washing Machine ({basket}): Finished washing')
    return f'{basket} is completed'

async def main():
   coroA = wash('Basket A')
   print(coroA)
   print(type(coroA))
   taskA = asyncio.create_task(coroA)
   print(taskA)
   print(type(taskA))
   resultA = await taskA
   coroB = wash('Basket B')
   print(coroB)
   print(type(coroB))
   taskB = asyncio.create_task(coroB)
   print(taskB)
   print(type(taskB))
   resultB = await taskB
   print(resultA)
   print(resultB)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')