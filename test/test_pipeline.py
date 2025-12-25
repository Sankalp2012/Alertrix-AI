import asyncio
from app.pipeline import run_alert_pipeline

async def test():
    alert = "is it not rainning in ghaziabad today"
    result = await run_alert_pipeline(alert)
    print(result)

asyncio.run(test())
