import httpx

async def fetch_url(url: str) -> str:
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            url,
            headers={
                "User-Agent": "AlertrixBot/1.0"
            }
        )
        response.raise_for_status()
        return response.text
