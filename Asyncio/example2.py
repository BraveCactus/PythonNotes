import asyncio

async def f1(x):
    print(x**1)
    await asyncio.sleep(2)
    print("Функция f1 завершила свою работу")

async def f2(x):
    print(x**2)
    await asyncio.sleep(2)
    print("Функция f2 завершила свою работу")

async def main():
    await asyncio.gather(f1(3), f2(3))
    # task1 = asyncio.create_task(f1(4))
    # task2 = asyncio.create_task(f1(5))

    # await task1
    # await task2

    

if __name__ == "__main__":
    asyncio.run(main())

   
