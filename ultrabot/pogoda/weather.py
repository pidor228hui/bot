import aiohttp
import asyncio
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

async def get_weather(city: str) -> str:
    url = f"https://yandex.ru/pogoda/{city}"

    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(headers=HEADERS, timeout=timeout) as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                 raise Exception("❌ Не удалось получить страницу")

            html = await resp.text()

    soup = BeautifulSoup(html, "html.parser")
    temp = soup.find("div", {"class": "main-content"})
    condition = soup.select_one("div", {"class": "condition"})

    if not temp or not condition:
        raise Exception("Город не найден")

    return f"{temp.text}C, {condition.text}"
