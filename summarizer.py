import openai
import os
from load_env import load_environment

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(content_blocks, query):
    print("[summarizer] Summarizing content...")

    combined_text = "\n\n".join([block["text"][:2000] for block in content_blocks])

    prompt = f"""
You are a research assistant. Your task is to read the following text and generate a concise summary in bullet points that directly answers the research query below.

Research Query:
"{query}"

Content:
"""
{combined_text}
"""

Give a clear, well-structured summary in under 300 words.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[summarizer] Error generating summary: {e}")
        return "Summary generation failed due to API error."