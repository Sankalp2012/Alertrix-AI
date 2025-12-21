import asyncio
from app.groq_client import groq_chat

async def test():
    out = await groq_chat([
        {"role": "system", "content": "Answer ONLY true or false."},
        {"role": "user", "content": "Is fire hot?"}
    ])
    print(out)

asyncio.run(test())
