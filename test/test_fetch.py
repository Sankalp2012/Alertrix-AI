import asyncio
from app.tools.fetch import fetch_url

async def test():
    html = await fetch_url("https://example.com")
    print(html[:300])  # print first 300 chars only

asyncio.run(test())
