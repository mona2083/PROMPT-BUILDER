# gemini_client.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
from storage import load_settings

load_dotenv()

AVAILABLE_MODELS = {
    "gemini": [
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-flash-latest",
        "gemini-pro-latest",
    ],
    "openai": [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
    ],
}

# 後方互換のためリストも用意
AVAILABLE_MODELS_FLAT = AVAILABLE_MODELS["gemini"] + AVAILABLE_MODELS["openai"]


def get_settings() -> dict:
    return load_settings()


def ask_gemini(prompt: str, model_name: str | None = None) -> str:
    """Gemini APIにプロンプトを送信して回答を返す。"""
    settings = get_settings()
    api_key = settings.get("api_key", "").strip() or os.getenv("GEMINI_API_KEY", "")
    if not api_key or api_key == "your_key_here":
        raise ValueError("Gemini APIキーが設定されていません")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name or settings.get("model", "gemini-2.5-flash"))
    response = model.generate_content(prompt)
    return response.text


def ask_openai(prompt: str, model_name: str | None = None) -> str:
    """OpenAI APIにプロンプトを送信して回答を返す。"""
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openaiライブラリが必要です: pip install openai")

    settings = get_settings()
    api_key = settings.get("openai_api_key", "").strip()
    if not api_key:
        raise ValueError("OpenAI APIキーが設定されていません")

    client = OpenAI(api_key=api_key)
    model = model_name or settings.get("openai_model", "gpt-4o-mini")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def ask_ai(prompt: str) -> str:
    """
    設定に応じてGeminiまたはOpenAIにプロンプトを送信する。
    """
    settings = get_settings()
    provider = settings.get("provider", "gemini")

    if provider == "openai":
        return ask_openai(prompt)
    else:
        return ask_gemini(prompt)