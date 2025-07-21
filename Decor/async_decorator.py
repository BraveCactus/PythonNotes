from typing import Callable, Coroutine
import time
from functools import wraps
import asyncio

"""Декораторы для асинхронных функций"""

def async_deco(cor: Coroutine):
    async def wrapper(*args, **kwargs):
        res = await cor(*args, **kwargs)
        return res
    return wrapper

@async_deco
async def func():
    await asyncio.sleep(1.5)
    return 1

if __name__ == "__main__":
    asyncio.run(func())




