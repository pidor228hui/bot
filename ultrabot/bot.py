import asyncio
import os
from dotenv import load_dotenv
from worker import bot_worker

load_dotenv()

all_tokens = [
    token.strip()
    for token in os.getenv("BOT_TOKENS", "").split(",")
    if token.strip()
]

async def main():
    tasks = [asyncio.create_task(bot_worker(t, all_tokens)) for t in all_tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
