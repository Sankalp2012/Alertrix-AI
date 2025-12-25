from app.tools.fetch import fetch_url
from app.utils.html_cleaner import clean_html
from app.utils.chunker import chunk_text
from app.summarizer import extract_facts
from app.reducer import consolidate_facts
from app.evaluator import evaluate_alert
from app.planner import plan_fetch_strategy

async def run_alert_pipeline(alert_text: str) -> bool:
    plan = await plan_fetch_strategy(alert_text)
    urls = plan.get("urls", [])

    all_facts = []

    for url in urls:
        html = await fetch_url(url)
        if not html:
            continue

        clean_text = clean_html(html)
        chunks = chunk_text(clean_text)

        for chunk in chunks:
            facts = await extract_facts(chunk, alert_text)
            if facts.strip():
                all_facts.append(facts)

    if not all_facts:
         return {
            "triggered": False,
            "confidence": 0.0,
            "reason": "No relevant data could be fetched",
            "assumptions": []
        }

    consolidated = await consolidate_facts(all_facts, alert_text)
    return await evaluate_alert(consolidated, alert_text)
