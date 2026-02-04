import asyncio
import os
from dotenv import load_dotenv
from worker import bot_worker
from core.decryptor import decrypt_tokens

load_dotenv()

enc_path = os.path.join("config", "tokens.enc")
master_key = os.getenv("MASTER_KEY", "")
all_tokens = decrypt_tokens(enc_path, master_key)

async def main():
    tasks = [asyncio.create_task(bot_worker(t, all_tokens)) for t in all_tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
