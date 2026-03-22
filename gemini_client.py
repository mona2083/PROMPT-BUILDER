# gemini_client.py

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from storage import load_settings

# Prefer new SDK (google-genai). Fall back to legacy google-generativeai if venv only has that
# (avoids: ImportError: cannot import name 'genai' from 'google').
try:
    from google import genai as _google_genai_sdk  # type: ignore[attr-defined]
except ImportError:
    _google_genai_sdk = None
if _google_genai_sdk is None:
    try:
        import google.generativeai as _google_generativeai_legacy  # type: ignore
    except ImportError:
        _google_generativeai_legacy = None
else:
    _google_generativeai_legacy = None

# Always load .env from the project root (next to this file), not from the process CWD.
# Gunicorn/systemd sometimes run with a different working directory, which breaks bare load_dotenv().
_PROJECT_ROOT = Path(__file__).resolve().parent
# utf-8-sig strips BOM; override=True so a blank GEMINI_API_KEY from the environment
# does not block values from .env
load_dotenv(_PROJECT_ROOT / ".env", encoding="utf-8-sig", override=True)


def _dotenv_var_name(name: str) -> str:
    """Strip BOM / whitespace so .env lines match GEMINI_API_KEY even if the file has a UTF-8 BOM on the first key."""
    return name.strip().lstrip("\ufeff").strip()


def _read_dotenv_manual(key: str) -> str:
    """If os.environ is missing the key, parse .env directly (handles odd server/Gunicorn cases)."""
    path = _PROJECT_ROOT / ".env"
    if not path.is_file():
        return ""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError:
        return ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].strip()
        if "=" not in line:
            continue
        name, _, val = line.partition("=")
        if _dotenv_var_name(name) != key:
            continue
        val = val.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        return val.strip()
    return ""


def _resolved_gemini_api_key(client_settings: Optional[dict], merged: dict) -> str:
    """
    1) Non-empty key from browser (client) wins.
    2) Then GEMINI_API_KEY from environment or .env file (deploy / demo).
    3) Then api_key from settings.json (merged), when client did not send a key.
    This avoids an empty or stale settings.json blocking .env.
    """
    cs = client_settings or {}
    raw = cs.get("api_key", "")
    client_key = str(raw).strip() if raw is not None else ""
    if client_key:
        return client_key
    env_or_file = (os.getenv("GEMINI_API_KEY") or "").strip() or _read_dotenv_manual("GEMINI_API_KEY")
    if env_or_file:
        return env_or_file
    return (merged.get("api_key") or "").strip()


def _resolved_openai_api_key(client_settings: Optional[dict], merged: dict) -> str:
    cs = client_settings or {}
    raw = cs.get("openai_api_key", "")
    client_key = str(raw).strip() if raw is not None else ""
    if client_key:
        return client_key
    env_or_file = (os.getenv("OPENAI_API_KEY") or "").strip() or _read_dotenv_manual("OPENAI_API_KEY")
    if env_or_file:
        return env_or_file
    return (merged.get("openai_api_key") or "").strip()


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
    for key in ["api_key", "openai_api_key", "model", "openai_model"]:
        val = client_settings.get(key, "")
        if val and str(val).strip():
            merged[key] = str(val).strip()
    # Provider: never switch to OpenAI from the browser unless they send an OpenAI key.
    # Otherwise localStorage can say provider=openai with empty keys while GEMINI_API_KEY works on the server.
    prov = (client_settings.get("provider") or "").strip()
    c_openai = (client_settings.get("openai_api_key") or "").strip()
    if prov == "openai" and c_openai:
        merged["provider"] = "openai"
    elif prov == "gemini":
        merged["provider"] = "gemini"
    # prov == "openai" without key → keep server provider (e.g. gemini + .env)
    return merged


def ask_gemini(prompt: str, client_settings: dict = None) -> str:
    settings = _merge_settings(client_settings)
    api_key = _resolved_gemini_api_key(client_settings, settings)
    if not api_key:
        raise ValueError("Gemini APIキーが設定されていません。設定画面からAPIキーを入力してください。")
    model_name = settings.get("model", "gemini-2.5-flash")

    if _google_genai_sdk is not None:
        client = _google_genai_sdk.Client(api_key=api_key)
        response = client.models.generate_content(model=model_name, contents=prompt)
        text = (response.text or "").strip()
    elif _google_generativeai_legacy is not None:
        _google_generativeai_legacy.configure(api_key=api_key)
        gm = _google_generativeai_legacy.GenerativeModel(model_name)
        response = gm.generate_content(prompt)
        text = (response.text or "").strip() if response.text else ""
    else:
        raise ImportError(
            "Gemini SDK が見つかりません。仮想環境で次を実行してください: "
            "pip install google-genai   "
            "（古いパッケージと競合する場合: pip uninstall google-generativeai && pip install google-genai）"
        )

    if not text:
        raise ValueError("Geminiから空の応答が返りました。モデル名やAPIの制限を確認してください。")
    return text


def ask_openai(prompt: str, client_settings: dict = None) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openaiライブラリが必要です: pip install openai")
    settings = _merge_settings(client_settings)
    api_key = _resolved_openai_api_key(client_settings, settings)
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
