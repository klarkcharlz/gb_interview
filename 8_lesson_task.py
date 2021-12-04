"""
По списку url реализовать загрузку страниц категорий с нашего проекта
и сохранение их в файлы.  Использовать asyncio и aiohttp.
"""
import aiohttp
import asyncio


URLS = ['http://127.0.0.1:8000/products/top/', 'http://127.0.0.1:8000/products/no_top/']


def write_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)


async def main():
    for url in URLS:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                second_loop = asyncio.get_event_loop()
                await second_loop.run_in_executor(None, write_file, f'{url.split("/")[-2]}.txt', html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
