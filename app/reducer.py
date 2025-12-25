from app.groq_client import groq_chat

async def consolidate_facts(facts: list[str], alert: str) -> str:
    combined = "\n".join(facts)
    messages = [
        {
            "role": "system",
            "content": (
                "Combine the following facts into a concise, non-redundant summary. "
                "Do not infer anything not explicitly stated."
            )
        },
        {
            "role": "user",
            "content": f"Alert:\n{alert}\n\nFacts:\n{combined}"
        }
    ]

    return await groq_chat(messages)
