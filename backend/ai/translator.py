import os
import google.generativeai as genai

# Configure once
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Single shared model instance
_model = genai.GenerativeModel("gemini-1.5-flash")

LANG_MAP = {
    "en": "English",
    "hi": "Hindi",
    "ta": "Tamil",
    "ml": "Malayalam",
    "te": "Telugu",
    "kn": "Kannada",
    "ja": "Japanese",
}


def translate_with_gemini(
    text: str,
    source_lang: str,
    target_lang: str
) -> str:
    if source_lang == target_lang:
        return text

    src = LANG_MAP.get(source_lang, "English")
    tgt = LANG_MAP.get(target_lang, "English")

    prompt = f"""
    Translate the following text from {src} to {tgt}.
    Return ONLY the translated text.

    Text:
    {text}
    """

    response = _model.generate_content(prompt)
    return response.text.strip()
