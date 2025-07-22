import asyncio
from typing import Coroutine

"""Данный декоратор проверяет не слишком ли долго устанавливает соединение с сервером, в противном случает бросает исключение"""

def deco_timeout(timeout: int):
    def wrapper(cor: Coroutine):
        async def inner(*args, **kwargs):
            nonlocal timeout
            try:
                result = await asyncio.wait_for(cor(*args, **kwargs), timeout = timeout)
                return result
            except asyncio.TimeoutError:
                print("Ошибка времени связи с сервером")            
        return inner
    return wrapper    


@deco_timeout(1.5)
async def connection(host, port):
    print(f"Началось соединение с сервером, host: {host}, port: {port}")
    await asyncio.sleep(2)
    print(f"Соединение с сервером установлено, host: {host}, port: {port}")
    return 42

async def main():
    await asyncio.gather(connection(1, 3), connection(2, 1))

if __name__ == "__main__":
    asyncio.run(main())
    
    