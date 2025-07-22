import asyncio

"""Программа имитирует подключение к какому-либо сервису, загрузку и выгрузку информация оттуда"""

# имитация  асинхронного соединения с некой периферией
async def get_connection(host, port):
    class Conn:
        async def put_data(self):
            print("Отправка данных...")
            await asyncio.sleep(2)
            print("Данные отправлены")

        async def get_data(self):
            print("Получение данных...")
            await asyncio.sleep(2)
            print("Данные получены")

        async def close(self):
            print("Закрытие соединения...")
            await asyncio.sleep(2)
            print("Соединение завершено")

    print('Устанавливаем соединение...')
    await asyncio.sleep(2)
    print('Соединение установлено.')
    return Conn()

class Connection:
    # этот конструктор будет неявно вызван в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_connection(self.host, self.port)
        return self.conn
    
    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

async def main():
    async with Connection('localhost', 9090) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        # операции отправки и получения данных выполняем конкурентно
        await send_task
        await receive_task

if __name__ == "__main__":
    asyncio.run(main())