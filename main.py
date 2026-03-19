# main.py — Flask版

import threading
import webbrowser
from flask import Flask, render_template, request, jsonify

from templates import LANG_UI, CATEGORIES, CATEGORY_KEY_MAP, TEMPLATES, build_prompt
from gemini_client import ask_ai, AVAILABLE_MODELS
from storage import (
    save_history, load_history, delete_history, clear_history,
    save_favorite, load_favorites, delete_favorite,
    load_settings, save_settings,
    load_presets, save_preset, delete_preset,
    load_profile, save_profile,
    load_profile_fields, save_profile_custom_field, delete_profile_custom_field,
    load_field_options, save_field_option, delete_field_option, load_all_field_options,
    load_instruction_presets, save_instruction_preset, delete_instruction_preset,
)

import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

# ────────────────────────────────────────────
# API エンドポイント
# ────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/fields")
def api_fields():
    category = request.args.get("category", "ai_pm")
    lang = request.args.get("lang", "ja")
    tmpl = TEMPLATES[category][lang]
    # storage.load_all_field_options() now returns all categories.
    # Keep API response backward-compatible for frontend by returning
    # only the selected category's field options.
    custom_options = load_all_field_options().get(category, {})
    return jsonify({
        "fields": tmpl["fields"],
        "custom_options": custom_options,
    })


@app.route("/api/build_prompt", methods=["POST"])
def api_build_prompt():
    from storage import get_profile_for_category
    data = request.json
    category = data["category"]
    profile = get_profile_for_category(category)
    prompt = build_prompt(
        category, data["lang"],
        data["user_inputs"],
        profile=profile,
        simple_mode=data.get("simple_mode", False),
        context_history=data.get("context_history", ""),
        instructions=data.get("instructions", ""),
        include_profile=data.get("include_profile", True),
        role_perspectives=data.get("role_perspectives", ""),
    )
    return jsonify({"prompt": prompt})


@app.route("/api/ask_ai", methods=["POST"])
def api_ask_ai():
    data = request.json
    try:
        # クライアントから送られたAPIキーを使用（なければサーバーのsettings.jsonにフォールバック）
        client_settings = {
            "api_key":        data.get("api_key", ""),
            "openai_api_key": data.get("openai_api_key", ""),
            "model":          data.get("model", ""),
            "openai_model":   data.get("openai_model", ""),
            "provider":       data.get("provider", ""),
        }
        answer = ask_ai(data["prompt"], client_settings=client_settings)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/save_history", methods=["POST"])
def api_save_history():
    data = request.json
    save_history(
        data["category"], data["lang"],
        data["prompt"], data.get("answer", "")
    )
    return jsonify({"ok": True})


@app.route("/api/history")
def api_history():
    return jsonify({"history": load_history()})


@app.route("/api/delete_history/<entry_id>", methods=["DELETE"])
def api_delete_history(entry_id):
    delete_history(entry_id)
    return jsonify({"ok": True})


@app.route("/api/clear_history", methods=["DELETE"])
def api_clear_history():
    clear_history()
    return jsonify({"ok": True})


@app.route("/api/save_favorite", methods=["POST"])
def api_save_favorite():
    data = request.json
    save_favorite(
        data["category"], data["lang"],
        data["prompt"], data.get("title", "")
    )
    return jsonify({"ok": True})


@app.route("/api/favorites")
def api_favorites():
    return jsonify({"favorites": load_favorites()})


@app.route("/api/delete_favorite/<entry_id>", methods=["DELETE"])
def api_delete_favorite(entry_id):
    delete_favorite(entry_id)
    return jsonify({"ok": True})


@app.route("/api/settings")
def api_settings():
    settings = load_settings()
    return jsonify({
        "api_key":          settings.get("api_key", ""),
        "openai_api_key":   settings.get("openai_api_key", ""),
        "model":            settings.get("model", "gemini-2.5-flash"),
        "openai_model":     settings.get("openai_model", "gpt-4o-mini"),
        "provider":         settings.get("provider", "gemini"),
        "gemini_models":    AVAILABLE_MODELS["gemini"],
        "openai_models":    AVAILABLE_MODELS["openai"],
    })


@app.route("/api/save_settings", methods=["POST"])
def api_save_settings():
    data = request.json
    settings = load_settings()
    settings["api_key"]        = data.get("api_key", "")
    settings["openai_api_key"] = data.get("openai_api_key", "")
    settings["model"]          = data.get("model", "gemini-2.5-flash")
    settings["openai_model"]   = data.get("openai_model", "gpt-4o-mini")
    settings["provider"]       = data.get("provider", "gemini")
    save_settings(settings)
    return jsonify({"ok": True})


@app.route("/api/presets")
def api_presets():
    category = request.args.get("category", "ai_pm")
    presets_by_category = load_presets().get(category, {})
    # Frontend expects a list of {id, name, fields}.
    presets = [
        {"id": name, "name": name, "fields": fields}
        for name, fields in presets_by_category.items()
    ]
    return jsonify({"presets": presets})


@app.route("/api/save_preset", methods=["POST"])
def api_save_preset():
    data = request.json
    save_preset(data["category"], data["name"], data["fields"])
    return jsonify({"ok": True})


@app.route("/api/delete_preset", methods=["DELETE"])
def api_delete_preset():
    data = request.json
    # Frontend sends preset_id; in current storage schema preset key is the name.
    preset_key = data.get("preset_id") or data.get("name")
    delete_preset(data["category"], preset_key)
    return jsonify({"ok": True})


@app.route("/api/profile")
def api_profile():
    from storage import PROFILE_GROUP_LABELS, PROFILE_GROUP_FIELDS
    return jsonify({
        "profile":      load_profile(),
        "fields":       load_profile_fields(),
        "group_labels": PROFILE_GROUP_LABELS,
        "group_keys":   list(PROFILE_GROUP_FIELDS.keys()),
    })


@app.route("/api/save_profile", methods=["POST"])
def api_save_profile():
    data = request.json
    save_profile(data["profile"])
    return jsonify({"ok": True})


@app.route("/api/add_profile_field", methods=["POST"])
def api_add_profile_field():
    data = request.json
    save_profile_custom_field(
        data.get("group", "common"), data["key"], data["label"]
    )
    return jsonify({"ok": True})


@app.route("/api/delete_profile_field", methods=["DELETE"])
def api_delete_profile_field():
    data = request.json
    delete_profile_custom_field(
        data.get("group", "common"), data["key"]
    )
    return jsonify({"ok": True})


# ── フィールドオプション ────────────────────
@app.route("/api/save_field_option", methods=["POST"])
def api_save_field_option():
    data = request.json
    save_field_option(data["category"], data["field_key"], data["value"])
    return jsonify({"ok": True})


@app.route("/api/delete_field_option", methods=["DELETE"])
def api_delete_field_option():
    data = request.json
    delete_field_option(data["category"], data["field_key"], data["value"])
    return jsonify({"ok": True})


@app.route("/api/custom_options_all")
def api_custom_options_all():
    import json, os
    filepath = "custom_options.json"
    if not os.path.exists(filepath):
        return jsonify({"custom_options": {}})
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify({"custom_options": data})

@app.route("/api/save_custom_option", methods=["POST"])
def api_save_custom_option():
    data = request.json
    save_custom_option(data["field_key"], data["value"])
    return jsonify({"ok": True})

@app.route("/api/delete_custom_option", methods=["DELETE"])
def api_delete_custom_option():
    data = request.json
    delete_custom_option(data["field_key"], data["value"])
    return jsonify({"ok": True})


# ── 指示プリセット ──────────────────────────
@app.route("/api/instruction_presets")
def api_instruction_presets():
    return jsonify({"presets": load_instruction_presets()})


@app.route("/api/save_instruction_preset", methods=["POST"])
def api_save_instruction_preset():
    data = request.json
    save_instruction_preset(
        data["key"], data["name"], data["instructions"]
    )
    return jsonify({"ok": True})


@app.route("/api/delete_instruction_preset", methods=["DELETE"])
def api_delete_instruction_preset():
    data = request.json
    delete_instruction_preset(data["key"])
    return jsonify({"ok": True})


# ────────────────────────────────────────────
# エントリーポイント
# ────────────────────────────────────────────
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    is_local = port == 5001
    if is_local:
        url = f"http://127.0.0.1:{port}"
        print(f"\n AI Prompt Builder 起動中...")
        print(f"   ブラウザで開く: {url}\n")
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(debug=False, host="0.0.0.0", port=port)
