import json
import re
from app.groq_client import groq_chat

def _extract_json(text: str) -> dict:
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON object found in planner response")
    return json.loads(match.group())

async def plan_fetch_strategy(alert_text: str) -> dict:
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI planner.\n"
                "Return ONLY a valid JSON object.\n"
                "Schema:\n"
                "{\n"
                '  "search_query": string,\n'
                '  "urls": string[]\n'
                "}\n"
                "No explanations. No markdown."
            )
        },
        {
            "role": "user",
            "content": alert_text
        }
    ]

    raw = await groq_chat(messages)
    return _extract_json(raw)
