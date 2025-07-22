import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print(f"Task {name}: computing factorial {number}, currently i = {i}")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial {number} = {f}")

async def main():

    async with asyncio.TaskGroup() as tg:
        tg.create_task(factorial("A", 2))
        tg.create_task(factorial("B", 3))
        tg.create_task(factorial("C", 4))
    # await asyncio.gather(factorial("A", 2),
    #                      factorial("B", 3),
    #                      factorial("C", 4))
    
if __name__ == "__main__":
    asyncio.run(main())