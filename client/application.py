import asyncio
from datetime import datetime
import json
import random
import string

from aiohttp import ClientSession
from aioconsole import aprint


class Client:
    url: str = "http://server:8000/messages"            # Адрес сервера внутри сети Docker
    symbols: str = string.ascii_letters + "123456789"   # Символы для генерации текста
    count_deleted_messages: int = 0                     # Количество удаленных сообщений
    delay_check: int = 10                               # Задержка вывода удаленных сообщений
    get_count_messages: int = 10                        # Количество получаеммых сообщений

    @staticmethod
    async def check_deleted_messages() -> None:
        while True:
            await asyncio.sleep(Client.delay_check)
            await aprint(
                f"{datetime.now().replace(microsecond=0)} - Удалено всего записей: {Client.count_deleted_messages}."
            )

    @staticmethod
    async def create() -> None:
        async with ClientSession() as session:
            while True:
                for _ in range(random.randint(10, 100)):
                    text = "".join(random.choice(Client.symbols) for _ in range(16))
                    await session.post(f"{Client.url}/new", json={"text": text})

    @staticmethod
    async def delete() -> None:
        async with ClientSession() as session:
            while True:
                response = await session.get(f"{Client.url}/{Client.get_count_messages}")
                for message in json.loads(await response.text()):
                    uuid = message.get("uuid")
                    res = await session.delete(f"{Client.url}/{uuid}")
                    if res.status == 200:
                        Client.count_deleted_messages += 1

    @staticmethod
    async def main():
        await asyncio.wait([
            asyncio.create_task(Client.create()),
            asyncio.create_task(Client.delete()),
            asyncio.create_task(Client.check_deleted_messages())
        ])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Client.main())
