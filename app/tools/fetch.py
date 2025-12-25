import httpx

async def fetch_url(url: str) -> str | None:
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as client:
            response = await client.get(
                url,
                headers={"User-Agent": "AlertrixBot/1.0"}
            )

            if response.status_code >= 400:
                return None

            return response.text

    except httpx.RequestError:
        return None
