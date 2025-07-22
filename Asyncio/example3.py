import asyncio
import time

async def say_after(what, delay):
    await asyncio.sleep(delay)
    print(what)

# async def main():
#     print(f"Started at time {time.strftime('%X')}")

#     task1 = asyncio.create_task(say_after("hello", 1))
#     task2 = asyncio.create_task(say_after("world", 2))

#     await task1
#     await task2

#     print(f"Ended at time {time.strftime('%X')}")

async def main():
    print(f"Started at time {time.strftime('%X')}")

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after("hello", 1))
        task2 = tg.create_task(say_after("world", 2))
        
    print(f"Ended at time {time.strftime('%X')}")
    print(type(asyncio.TaskGroup()))



if __name__ == "__main__":
    asyncio.run(main())


