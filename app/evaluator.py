import json
from app.groq_client import groq_chat

async def evaluate_alert(summary: str, alert_text: str) -> dict:
    messages = [
        {
            "role": "system",
            "content": (
                "You are an alert evaluator.\n"
                "Given a user alert and factual summary, decide whether the alert "
                "should be considered triggered.\n\n"
                "IMPORTANT RULES:\n"
                "- Do NOT assume strict numeric thresholds unless explicitly stated.\n"
                "- Consider nearby locations or related context only if reasonable.\n"
                "- If assumptions are made, list them.\n"
                "- Be conservative if facts do not clearly satisfy the alert.\n\n"
                "Return ONLY valid JSON in this format:\n"
                "{\n"
                '  "triggered": boolean,\n'
                '  "confidence": number between 0 and 1,\n'
                '  "reason": string,\n'
                '  "assumptions": string[]\n'
                "}"
            )
        },
        {
            "role": "user",
            "content": (
                f"Alert:\n{alert_text}\n\n"
                f"Factual summary:\n{summary}"
            )
        }
    ]

    raw = await groq_chat(messages)
    # Strict JSON extraction
    start = raw.find("{")
    end = raw.rfind("}") + 1
    parsed = json.loads(raw[start:end])

    return parsed
