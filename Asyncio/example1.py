import asyncio
import time 

async def one():
    print("Start one")
    await asyncio.sleep(4)
    print("Finish one")

async def two():
    print("Start two")
    await asyncio.sleep(2)
    print("Finish two")

async def three():
    print("Start three")
    await asyncio.sleep(3)
    print("Finish three")

async def main():
    await asyncio.gather(one(), two(), three())
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # await asyncio.create_task(three())

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Time: {time.time() - start}")