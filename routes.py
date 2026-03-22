# routes.py — API routes (Flask blueprint)

import os

from flask import Blueprint, render_template, request, jsonify

from templates import TEMPLATES, build_prompt
from gemini_client import ask_ai, AVAILABLE_MODELS
import storage

bp = Blueprint("prompt_builder_routes", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/fields")
def api_fields():
    category = request.args.get("category", "ai_pm")
    lang = request.args.get("lang", "ja")
    tmpl = TEMPLATES[category][lang]
    custom_options = storage.load_all_field_options(category)
    return jsonify({"fields": tmpl["fields"], "custom_options": custom_options})


@bp.route("/api/build_prompt", methods=["POST"])
def api_build_prompt():
    data = request.json
    category = data["category"]
    profile = storage.get_profile_for_category(category)
    prompt = build_prompt(
        category,
        data["lang"],
        data["user_inputs"],
        profile=profile,
        simple_mode=data.get("simple_mode", False),
        context_history=data.get("context_history", ""),
        instructions=data.get("instructions", ""),
        include_profile=data.get("include_profile", True),
        role_perspectives=data.get("role_perspectives", ""),
    )
    return jsonify({"prompt": prompt})


@bp.route("/api/ask_ai", methods=["POST"])
def api_ask_ai():
    data = request.json
    try:
        client_settings = {
            "api_key": data.get("api_key", ""),
            "openai_api_key": data.get("openai_api_key", ""),
            "model": data.get("model", ""),
            "openai_model": data.get("openai_model", ""),
            "provider": data.get("provider", ""),
        }
        answer = ask_ai(data["prompt"], client_settings=client_settings)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)})


@bp.route("/api/save_history", methods=["POST"])
def api_save_history():
    data = request.json
    storage.save_history(data["category"], data["lang"], data["prompt"], data.get("answer", ""))
    return jsonify({"ok": True})


@bp.route("/api/history")
def api_history():
    return jsonify({"history": storage.load_history()})


@bp.route("/api/delete_history/<entry_id>", methods=["DELETE"])
def api_delete_history(entry_id):
    storage.delete_history(entry_id)
    return jsonify({"ok": True})


@bp.route("/api/clear_history", methods=["DELETE"])
def api_clear_history():
    storage.clear_history()
    return jsonify({"ok": True})


@bp.route("/api/save_favorite", methods=["POST"])
def api_save_favorite():
    data = request.json
    storage.save_favorite(
        data["category"],
        data["lang"],
        data["prompt"],
        data.get("title", ""),
    )
    return jsonify({"ok": True})


@bp.route("/api/favorites")
def api_favorites():
    return jsonify({"favorites": storage.load_favorites()})


@bp.route("/api/delete_favorite/<entry_id>", methods=["DELETE"])
def api_delete_favorite(entry_id):
    storage.delete_favorite(entry_id)
    return jsonify({"ok": True})


@bp.route("/api/settings")
def api_settings():
    settings = storage.load_settings()
    gemini_file = bool((settings.get("api_key") or "").strip())
    gemini_env = bool((os.getenv("GEMINI_API_KEY") or "").strip())
    openai_ok = bool((settings.get("openai_api_key") or "").strip() or (os.getenv("OPENAI_API_KEY") or "").strip())
    use_server_defaults_available = gemini_file or gemini_env or openai_ok
    return jsonify(
        {
            "api_key": settings.get("api_key", ""),
            "openai_api_key": settings.get("openai_api_key", ""),
            "model": settings.get("model", "gemini-2.5-flash"),
            "openai_model": settings.get("openai_model", "gpt-4o-mini"),
            "provider": settings.get("provider", "gemini"),
            "gemini_models": AVAILABLE_MODELS["gemini"],
            "openai_models": AVAILABLE_MODELS["openai"],
            "use_server_defaults_available": use_server_defaults_available,
        }
    )


@bp.route("/api/save_settings", methods=["POST"])
def api_save_settings():
    data = request.json
    settings = storage.load_settings()
    settings["api_key"] = data.get("api_key", "")
    settings["openai_api_key"] = data.get("openai_api_key", "")
    settings["model"] = data.get("model", "gemini-2.5-flash")
    settings["openai_model"] = data.get("openai_model", "gpt-4o-mini")
    settings["provider"] = data.get("provider", "gemini")
    storage.save_settings(settings)
    return jsonify({"ok": True})


@bp.route("/api/presets")
def api_presets():
    category = request.args.get("category", "ai_pm")
    return jsonify({"presets": storage.load_presets(category)})


@bp.route("/api/save_preset", methods=["POST"])
def api_save_preset():
    data = request.json
    storage.save_preset(data["category"], data["name"], data["fields"])
    return jsonify({"ok": True})


@bp.route("/api/delete_preset", methods=["DELETE"])
def api_delete_preset():
    data = request.json
    storage.delete_preset(data["category"], data["preset_id"])
    return jsonify({"ok": True})


@bp.route("/api/profile")
def api_profile():
    return jsonify(
        {
            "profile": storage.load_profile(),
            "fields": storage.load_profile_fields(),
            "group_labels": storage.PROFILE_GROUP_LABELS,
            "group_keys": list(storage.PROFILE_GROUP_FIELDS.keys()),
        }
    )


@bp.route("/api/save_profile", methods=["POST"])
def api_save_profile():
    data = request.json
    storage.save_profile(data["profile"])
    return jsonify({"ok": True})


@bp.route("/api/add_profile_field", methods=["POST"])
def api_add_profile_field():
    data = request.json
    storage.save_profile_custom_field(data.get("group", "common"), data["key"], data["label"])
    return jsonify({"ok": True})


@bp.route("/api/delete_profile_field", methods=["DELETE"])
def api_delete_profile_field():
    data = request.json
    storage.delete_profile_custom_field(data.get("group", "common"), data["key"])
    return jsonify({"ok": True})


@bp.route("/api/save_field_option", methods=["POST"])
def api_save_field_option():
    data = request.json
    storage.save_field_option(data["category"], data["field_key"], data["value"])
    return jsonify({"ok": True})


@bp.route("/api/delete_field_option", methods=["DELETE"])
def api_delete_field_option():
    data = request.json
    storage.delete_field_option(data["category"], data["field_key"], data["value"])
    return jsonify({"ok": True})


@bp.route("/api/custom_options_all")
def api_custom_options_all():
    return jsonify({"custom_options": storage.load_custom_options()})


@bp.route("/api/save_custom_option", methods=["POST"])
def api_save_custom_option():
    data = request.json
    storage.save_custom_option(data["field_key"], data["value"])
    return jsonify({"ok": True})


@bp.route("/api/delete_custom_option", methods=["DELETE"])
def api_delete_custom_option():
    data = request.json
    storage.delete_custom_option(data["field_key"], data["value"])
    return jsonify({"ok": True})


@bp.route("/api/instruction_presets")
def api_instruction_presets():
    return jsonify({"presets": storage.load_instruction_presets()})


@bp.route("/api/save_instruction_preset", methods=["POST"])
def api_save_instruction_preset():
    data = request.json
    storage.save_instruction_preset(data["key"], data["name"], data["instructions"])
    return jsonify({"ok": True})


@bp.route("/api/delete_instruction_preset", methods=["DELETE"])
def api_delete_instruction_preset():
    data = request.json
    storage.delete_instruction_preset(data["key"])
    return jsonify({"ok": True})

