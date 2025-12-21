from app.groq_client import groq_chat

async def is_alert_triggered(facts: str, condition: str) -> bool:
    messages = [
        {
            "role": "system",
            "content": "Answer ONLY true or false based on the facts provided."
        },
        {
            "role": "user",
            "content": f"Facts:\n{facts}\n\nCondition:\n{condition}"
        }
    ]

    result = await groq_chat(messages)
    return result.strip().lower().startswith("true")
