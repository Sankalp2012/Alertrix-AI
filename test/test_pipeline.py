import asyncio
from app.pipeline import run_alert_pipeline

async def test():
    alert = "did it rained in vrindavan today"
    result = await run_alert_pipeline(alert)
    print(result)

asyncio.run(test())
