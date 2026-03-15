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
        "gemini-2.0-flash",
        "gemini-1.5-flash",
    ],
    "openai": [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
    ],
}

AVAILABLE_MODELS_FLAT = AVAILABLE_MODELS["gemini"] + AVAILABLE_MODELS["openai"]


def _merge_settings(client_settings: dict = None) -> dict:
    """サーバーのsettingsにクライアントの値をマージ（クライアント優先）。"""
    server = load_settings()
    if not client_settings:
        return server
    merged = dict(server)
    for key in ["api_key", "openai_api_key", "model", "openai_model", "provider"]:
        val = client_settings.get(key, "")
        if val and str(val).strip():
            merged[key] = str(val).strip()
    return merged


def ask_gemini(prompt: str, client_settings: dict = None) -> str:
    settings = _merge_settings(client_settings)
    api_key = settings.get("api_key", "").strip() or os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        raise ValueError("Gemini APIキーが設定されていません。設定画面からAPIキーを入力してください。")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(settings.get("model", "gemini-2.5-flash"))
    response = model.generate_content(prompt)
    return response.text


def ask_openai(prompt: str, client_settings: dict = None) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openaiライブラリが必要です: pip install openai")
    settings = _merge_settings(client_settings)
    api_key = settings.get("openai_api_key", "").strip()
    if not api_key:
        raise ValueError("OpenAI APIキーが設定されていません。設定画面からAPIキーを入力してください。")
    client = OpenAI(api_key=api_key)
    model = settings.get("openai_model", "gpt-4o-mini")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def ask_ai(prompt: str, client_settings: dict = None) -> str:
    settings = _merge_settings(client_settings)
    provider = settings.get("provider", "gemini")
    if provider == "openai":
        return ask_openai(prompt, client_settings=client_settings)
    else:
        return ask_gemini(prompt, client_settings=client_settings)