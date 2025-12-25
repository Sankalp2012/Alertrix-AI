import asyncio
from app.summarizer import summarize_facts

async def test():
    raw = """
    Delhi AQI today reached 512 according to the Central Pollution Control Board.
    Health emergency declared. Schools advised to close.
    """
    alert = "Notify me when AQI goes above 500 in Delhi."

    summary = await summarize_facts(raw, alert)
    print(summary)

asyncio.run(test())
