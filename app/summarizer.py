from app.groq_client import groq_chat

async def extract_facts(chunk: str, alert: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Extract ONLY concrete factual statements relevant to the alert. "
                "Ignore opinions, navigation text, ads, unrelated info."
            )
        },
        {
            "role": "user",
            "content": f"Alert:\n{alert}\n\nText:\n{chunk}"
        }
    ]

    return await groq_chat(messages)
