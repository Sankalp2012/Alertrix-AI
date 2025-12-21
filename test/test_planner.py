import asyncio
from app.planner import plan_fetch_strategy

async def test():
    alert = "Notify me when the cricket match restarts after rain."
    plan = await plan_fetch_strategy(alert)

    print(plan)

    assert "search_query" in plan
    assert "urls" in plan
    assert isinstance(plan["urls"], list)

asyncio.run(test())
