# backend/services/gemma_translate.py

import os
from google import genai

# ✅ Only ONE key source
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not set")

# ✅ Correct client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"  # ✅ NO 'models/' prefix

def translate_with_gemini(text: str, source_lang: str, target_lang: str) -> str:
    prompt = f"""
Translate the following text from {source_lang} to {target_lang}.
Return ONLY the translated text.

Text:
{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text.strip()
