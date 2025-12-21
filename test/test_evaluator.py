import asyncio
from app.evaluator import is_alert_triggered

async def test():
    facts = "The cricket match was stopped due to rain. Play resumed at 4:30 PM."
    condition = "Notify me when the cricket match restarts after rain."

    triggered = await is_alert_triggered(facts, condition)
    print(triggered)

asyncio.run(test())
