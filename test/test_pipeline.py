import asyncio
from app.pipeline import run_alert_pipeline

async def test():
    alert = "Notify me when the cricket match restarts after rain."
    result = await run_alert_pipeline(alert)
    print(result)

asyncio.run(test())
