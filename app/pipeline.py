from app.planner import plan_fetch_strategy
from app.tools.fetch import fetch_url
from app.evaluator import is_alert_triggered

async def run_alert_pipeline(alert_text: str) -> bool:
    # 1) Plan
    plan = await plan_fetch_strategy(alert_text)

    urls = plan.get("urls", [])

    all_data = ""

    # 2) Fetch data
    for url in urls:
        try:
            content = await fetch_url(url)
            all_data += content + "\n"
        except Exception:
            continue

    # 3) Evaluate
    return await is_alert_triggered(all_data, alert_text)
