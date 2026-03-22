# storage.py

import json
import os
from pathlib import Path

# All JSON paths are anchored to this package directory (not the process CWD).
# Gunicorn/systemd may use a CWD where these files do not exist.
_DATA_DIR = Path(__file__).resolve().parent


def _data_file(name: str) -> str:
    return str(_DATA_DIR / name)

# ────────────────────────────────────────────
# 汎用ユーティリティ
# ────────────────────────────────────────────
def _load(path: str, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(path: str, data) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ────────────────────────────────────────────
# 履歴
# ────────────────────────────────────────────
HISTORY_FILE = _data_file("history.json")
MAX_HISTORY = 100

def save_history(category: str, lang: str, prompt: str, answer: str = "") -> None:
    history = _load(HISTORY_FILE, [])
    history.insert(0, {
        "category": category, "lang": lang,
        "prompt": prompt, "answer": answer,
        "ts": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
    })
    _save(HISTORY_FILE, history[:MAX_HISTORY])

def load_history() -> list:
    return _load(HISTORY_FILE, [])

def delete_history(index: int) -> None:
    history = _load(HISTORY_FILE, [])
    if 0 <= index < len(history):
        history.pop(index)
        _save(HISTORY_FILE, history)

def clear_history() -> None:
    _save(HISTORY_FILE, [])


# ────────────────────────────────────────────
# お気に入り
# ────────────────────────────────────────────
FAVORITES_FILE = _data_file("favorites.json")

def save_favorite(category: str, lang: str, prompt: str, answer: str = "") -> None:
    favs = _load(FAVORITES_FILE, [])
    favs.insert(0, {
        "category": category, "lang": lang,
        "prompt": prompt, "answer": answer,
        "ts": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
    })
    _save(FAVORITES_FILE, favs)

def load_favorites() -> list:
    return _load(FAVORITES_FILE, [])

def delete_favorite(index: int) -> None:
    favs = _load(FAVORITES_FILE, [])
    if 0 <= index < len(favs):
        favs.pop(index)
        _save(FAVORITES_FILE, favs)


# ────────────────────────────────────────────
# 設定
# ────────────────────────────────────────────
SETTINGS_FILE = _data_file("settings.json")

def load_settings() -> dict:
    return _load(SETTINGS_FILE, {})

def save_settings(settings: dict) -> None:
    _save(SETTINGS_FILE, settings)


# ────────────────────────────────────────────
# プリセット
# ────────────────────────────────────────────
PRESETS_FILE = _data_file("presets.json")

def load_presets() -> dict:
    return _load(PRESETS_FILE, {})

def save_preset(category: str, name: str, inputs: dict) -> None:
    presets = load_presets()
    if category not in presets:
        presets[category] = {}
    presets[category][name] = inputs
    _save(PRESETS_FILE, presets)

def delete_preset(category: str, name: str) -> None:
    presets = load_presets()
    if category in presets and name in presets[category]:
        del presets[category][name]
        _save(PRESETS_FILE, presets)


# ────────────────────────────────────────────
# フィールド別カスタム選択肢
# ────────────────────────────────────────────
FIELD_OPTIONS_FILE = _data_file("field_options.json")

def load_field_options(category: str, field_key: str) -> list:
    all_opts = _load(FIELD_OPTIONS_FILE, {})
    return all_opts.get(category, {}).get(field_key, [])

def load_all_field_options() -> dict:
    return _load(FIELD_OPTIONS_FILE, {})

def save_field_option(category: str, field_key: str, value: str) -> None:
    all_opts = _load(FIELD_OPTIONS_FILE, {})
    if category not in all_opts:
        all_opts[category] = {}
    if field_key not in all_opts[category]:
        all_opts[category][field_key] = []
    if value not in all_opts[category][field_key]:
        all_opts[category][field_key].append(value)
    _save(FIELD_OPTIONS_FILE, all_opts)

def delete_field_option(category: str, field_key: str, value: str) -> None:
    all_opts = _load(FIELD_OPTIONS_FILE, {})
    if category in all_opts and field_key in all_opts[category]:
        all_opts[category][field_key] = [
            v for v in all_opts[category][field_key] if v != value
        ]
        _save(FIELD_OPTIONS_FILE, all_opts)


# ────────────────────────────────────────────
# AIへの指示プリセット
# ────────────────────────────────────────────
INSTRUCTIONS_FILE = _data_file("instructions.json")

DEFAULT_INSTRUCTION_PRESETS = {
    "general": {
        "name": {"ja": "基本ルール（汎用）", "en": "General Rules"},
        "instructions": [
            {"ja": "回答は簡潔かつ具体的にしてください。抽象的な表現は避け、実例や数値を使って説明してください。", "en": "Keep answers concise and specific. Avoid abstract expressions; use examples and numbers."},
            {"ja": "不確かな情報や推測を述べる場合は、必ず「〜かもしれません」「〜と考えられます」などと明示してください。", "en": "When stating uncertain information or guesses, always flag it explicitly with phrases like 'this may be' or 'it is thought that'."},
            {"ja": "回答の最後に、次に確認すべき点や推奨アクションを1〜2点追加してください。", "en": "At the end of your answer, add 1-2 next steps or recommended actions."},
        ]
    },
    "accuracy": {
        "name": {"ja": "精度・信頼性重視", "en": "Accuracy & Reliability"},
        "instructions": [
            {"ja": "主張には必ず根拠（出典・理論・実績）を添えてください。", "en": "Always provide evidence (sources, theory, track record) for any claim."},
            {"ja": "「絶対に」「必ず」などの断定表現は、確実な根拠がある場合のみ使用してください。", "en": "Only use absolute terms like 'always' or 'definitely' when there is solid evidence."},
            {"ja": "複数の解釈や方法がある場合は、それぞれのトレードオフを明示してください。", "en": "When multiple interpretations or methods exist, explicitly state the trade-offs of each."},
        ]
    },
    "reasoning": {
        "name": {"ja": "思考・推論プロセス重視", "en": "Reasoning Process"},
        "instructions": [
            {"ja": "結論を述べる前に、考え方のプロセスをステップごとに説明してください。", "en": "Before stating a conclusion, explain the reasoning process step by step."},
            {"ja": "複数の選択肢を検討した上で、最も適切な回答を選んだ理由を説明してください。", "en": "Consider multiple options and explain why you chose the most appropriate answer."},
            {"ja": "反論や代替案も検討し、それらを排除した理由も示してください。", "en": "Also consider counterarguments or alternatives, and explain why they were ruled out."},
        ]
    },
    "code": {
        "name": {"ja": "コード作業用", "en": "Code Work"},
        "instructions": [
            {"ja": "コードは必ずコードブロック（```）で囲んでください。", "en": "Always wrap code in code blocks (```)."},
            {"ja": "型ヒント（Type hints）を全関数に付けてください（Pythonの場合）。", "en": "Add type hints to all functions (for Python)."},
            {"ja": "コードの変更点は差分形式（変更前・変更後）で示してください。", "en": "Show code changes in diff format (before/after)."},
            {"ja": "依頼していないコードは書かないでください。まず問題を理解してから実装を提案してください。", "en": "Do not write code that was not requested. Understand the problem first, then propose an implementation."},
        ]
    },
    "language": {
        "name": {"ja": "語学学習用", "en": "Language Learning"},
        "instructions": [
            {"ja": "例文は必ず実際の会話で使える自然な表現にしてください。", "en": "Example sentences must be natural expressions usable in real conversation."},
            {"ja": "文法の説明は簡潔にし、実用的な使い方を優先してください。", "en": "Keep grammar explanations brief; prioritize practical usage."},
            {"ja": "よくある間違いやニュアンスの違いがある場合は必ず補足してください。", "en": "Always add notes on common mistakes or nuance differences when relevant."},
        ]
    },
    "format": {
        "name": {"ja": "出力フォーマット重視", "en": "Output Format"},
        "instructions": [
            {"ja": "マークダウン記法（**太字**、## 見出し、- 箇条書き）を使って読みやすく整形してください。", "en": "Use markdown formatting (**bold**, ## headers, - bullets) to make the output readable."},
            {"ja": "長い回答は「結論→根拠→詳細」の順に構成してください。", "en": "Structure long answers as: Conclusion → Evidence → Details."},
            {"ja": "数値データがある場合は表形式で示してください。", "en": "Present numerical data in table format when applicable."},
        ]
    },
}

def load_instruction_presets() -> dict:
    custom = _load(INSTRUCTIONS_FILE, {})
    merged = dict(DEFAULT_INSTRUCTION_PRESETS)
    merged.update(custom)
    return merged

def save_instruction_preset(key: str, name, instructions: list) -> None:
    custom = _load(INSTRUCTIONS_FILE, {})
    custom[key] = {"name": name, "instructions": instructions}
    _save(INSTRUCTIONS_FILE, custom)

def delete_instruction_preset(key: str) -> None:
    custom = _load(INSTRUCTIONS_FILE, {})
    if key in custom:
        del custom[key]
        _save(INSTRUCTIONS_FILE, custom)


# ────────────────────────────────────────────
# グループ別プロフィール
# ────────────────────────────────────────────
PROFILE_FILE = _data_file("profile.json")

# カテゴリ → プロフィールグループのマッピング
CATEGORY_PROFILE_MAP = {
    "ai_pm":    ["common", "tech"],
    "code":     ["common", "tech"],
    "app_dev":  ["common", "tech"],
    "ai_ml":    ["common", "tech"],
    "health":   ["common", "life"],
    "recipe":   ["common", "recipe"],
    "study":    ["common", "study"],
    "language": ["common", "study"],
    "chat":     ["common"],
    "other":    ["common"],
}

# グループ表示名（JA/EN辞書形式）
PROFILE_GROUP_LABELS = {
    "common": {"ja": "共通（全カテゴリ）",  "en": "Common (All)"},
    "tech":   {"ja": "PC・技術系",          "en": "Tech & Dev"},
    "life":   {"ja": "生活・健康",          "en": "Life & Health"},
    "recipe": {"ja": "料理・食事",          "en": "Cooking & Food"},
    "study":  {"ja": "学習系",              "en": "Study & Language"},
}

# グループ別フィールド定義 (field_key, label_dict, placeholder_dict)
PROFILE_GROUP_FIELDS = {
    "common": [
        ("name",         {"ja": "名前 / 呼び方",          "en": "Name"},            {"ja": "例: Manami",              "en": "e.g. Manami"}),
        ("age",          {"ja": "年齢・ライフステージ",    "en": "Age / Life Stage"}, {"ja": "例: 30代・社会人",         "en": "e.g. 30s, working professional"}),
        ("occupation",   {"ja": "職業・役職",              "en": "Occupation"},       {"ja": "例: AIエンジニア・PM",     "en": "e.g. AI Engineer / PM"}),
        ("native_lang",  {"ja": "母語 / 日常使用言語",     "en": "Native Language"},  {"ja": "例: 日本語",              "en": "e.g. Japanese"}),
        ("answer_style", {"ja": "回答スタイルの好み",       "en": "Preferred Style"},  {"ja": "例: 箇条書きで簡潔に",    "en": "e.g. Concise bullet points"}),
        ("other",        {"ja": "その他・備考",             "en": "Notes"},            {"ja": "例: 基本的に丁寧語で",    "en": "e.g. Keep it formal"}),
    ],
    "tech": [
        ("os",          {"ja": "作業環境（OS）",           "en": "OS / Environment"}, {"ja": "例: macOS 14 / Apple Silicon",     "en": "e.g. macOS 14 / Apple Silicon"}),
        ("main_lang",   {"ja": "主な使用言語",             "en": "Main Language"},    {"ja": "例: Python・TypeScript",           "en": "e.g. Python, TypeScript"}),
        ("experience",  {"ja": "経験職種と年数",           "en": "Experience"},       {"ja": "例: バックエンド5年 / ML2年",      "en": "e.g. Backend 5yr / ML 2yr"}),
        ("dev_env",     {"ja": "メイン開発環境",           "en": "Dev Environment"},  {"ja": "例: VSCode / Docker / GitHub",     "en": "e.g. VSCode / Docker / GitHub"}),
        ("tech_rules",  {"ja": "最低要求・ルール",         "en": "Rules / Requirements"}, {"ja": "例: コードは依頼するまで書かないで", "en": "e.g. Don't write code unless asked"}),
        ("tech_level",  {"ja": "技術レベル",               "en": "Tech Level"},       {"ja": "例: 中級・本番経験あり",           "en": "e.g. Intermediate, production exp."}),
    ],
    "life": [
        ("lifestyle",    {"ja": "生活スタイル",             "en": "Lifestyle"},        {"ja": "例: 在宅勤務・一人暮らし",         "en": "e.g. Remote work, living alone"}),
        ("hobbies",      {"ja": "趣味・好きなこと",         "en": "Hobbies"},          {"ja": "例: 料理・ヨガ・読書",            "en": "e.g. Cooking, yoga, reading"}),
        ("personality",  {"ja": "性格",                    "en": "Personality"},       {"ja": "例: 几帳面・計画的",              "en": "e.g. Detail-oriented, organized"}),
        ("health_notes", {"ja": "健康目標・気をつけていること", "en": "Health Goals"},  {"ja": "例: 塩分控えめ・週3運動",         "en": "e.g. Low sodium, exercise 3x/week"}),
        ("household",    {"ja": "家族構成・人数",           "en": "Household"},        {"ja": "例: 1人暮らし",                  "en": "e.g. Living alone"}),
    ],
    "recipe": [
        ("living_env",    {"ja": "生活環境・居住地",         "en": "Living Environment"}, {"ja": "例: ハワイ在住・アジア系スーパーあり", "en": "e.g. Hawaii, Asian grocery nearby"}),
        ("food_likes",    {"ja": "好きな料理・食の好み",      "en": "Food Likes"},         {"ja": "例: 日本食・スパイシー好き・あっさり系", "en": "e.g. Japanese food, spicy, light flavors"}),
        ("food_dislikes", {"ja": "苦手な食材・避けたいもの",  "en": "Food Dislikes"},      {"ja": "例: 甘いもの全般・牛乳（豆乳はOK）・パクチー", "en": "e.g. Sweets, dairy milk (soy milk OK), cilantro"}),
        ("allergies",     {"ja": "アレルギー・食事制限",      "en": "Allergies"},          {"ja": "例: なし / 乳製品アレルギー",     "en": "e.g. None / Dairy allergy"}),
        ("staple_pantry", {"ja": "常備調味料",               "en": "Pantry Staples"},     {"ja": "例: 醤油・みりん・オリーブオイル", "en": "e.g. Soy sauce, mirin, olive oil"}),
        ("staple_food",   {"ja": "常備食材",                 "en": "Staple Ingredients"}, {"ja": "例: 卵・玉ねぎ・にんにく・米",   "en": "e.g. Eggs, onion, garlic, rice"}),
        ("kitchen_tools", {"ja": "持っている調理器具",        "en": "Kitchen Tools"},      {"ja": "例: フライパン・炊飯器・オーブン", "en": "e.g. Frying pan, rice cooker, oven"}),
    ],
    "study": [
        ("major",       {"ja": "専攻・学部",               "en": "Major / Program"},  {"ja": "例: 経済学部2年",              "en": "e.g. Economics Year 2"}),
        ("study_level", {"ja": "現在の学習レベル",         "en": "Study Level"},      {"ja": "例: 統計基礎は理解済み",        "en": "e.g. Basics understood"}),
        ("study_style", {"ja": "学習スタイルの好み",       "en": "Learning Style"},   {"ja": "例: 具体例から入ってほしい",    "en": "e.g. Start with examples"}),
        ("target_lang", {"ja": "学習中の言語",             "en": "Target Language"},  {"ja": "例: 英語・スペイン語",          "en": "e.g. English, Spanish"}),
        ("lang_level",  {"ja": "語学レベル",               "en": "Language Level"},   {"ja": "例: TOEIC700・日常会話可",      "en": "e.g. TOEIC 700, daily conversation"}),
        ("study_goal",  {"ja": "学習目標",                 "en": "Study Goal"},       {"ja": "例: 来年IELTS7.0取得",          "en": "e.g. IELTS 7.0 next year"}),
        ("study_rules", {"ja": "学習のルール・希望",       "en": "Study Rules"},      {"ja": "例: 答えを直接教えないで",      "en": "e.g. Don't give direct answers"}),
    ],
}


def migrate_profile(profile: dict) -> dict:
    """旧形式のカスタムフィールド値を新形式 {label, value} に変換する。"""
    raw_custom = profile.get("_custom_fields", {})
    if isinstance(raw_custom, list):
        raw_custom = {}
        profile["_custom_fields"] = raw_custom

    changed = False
    for group, customs in raw_custom.items():
        if not isinstance(customs, list):
            continue
        group_data = profile.get(group, {})
        for cf in customs:
            key = cf.get("key", "")
            label = cf.get("label", "")
            if not key or not label:
                continue
            val = group_data.get(key)
            # 旧形式（文字列）のままなら新形式に変換
            if val is not None and isinstance(val, str):
                group_data[key] = {"label": label, "value": val}
                changed = True
        profile[group] = group_data

    if changed:
        _save(PROFILE_FILE, profile)
    return profile


def load_profile() -> dict:
    """プロフィール全体を返す。"""
    if not os.path.exists(PROFILE_FILE):
        return {"common": {}, "tech": {}, "life": {}, "recipe": {}, "study": {}, "_custom_fields": {}}
    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    for g in ["common", "tech", "life", "recipe", "study"]:
        if g not in data:
            data[g] = {}
    if "_custom_fields" not in data:
        data["_custom_fields"] = {}
    # 旧形式を自動マイグレーション
    data = migrate_profile(data)
    return data


def save_profile(profile: dict) -> None:
    _save(PROFILE_FILE, profile)


def get_profile_for_category(category: str) -> dict:
    """カテゴリに対応するプロフィールをラベル付きで返す。"""
    profile = load_profile()
    fields_by_group = load_profile_fields()
    groups = CATEGORY_PROFILE_MAP.get(category, ["common"])
    result = {}

    raw_custom = profile.get("_custom_fields", {})
    if isinstance(raw_custom, list):
        raw_custom = {}

    for group in groups:
        group_data = profile.get(group, {})
        group_fields = fields_by_group.get(group, [])

        # デフォルトフィールド: キー → ラベル
        key_to_label = {}
        for field in group_fields:
            key = field[0]
            label = field[1]
            if isinstance(label, dict):
                display_label = label.get("ja") or label.get("en") or key
            else:
                display_label = label or key
            key_to_label[key] = display_label

        # カスタムフィールド: キー → ユーザーが入力したラベル名
        for cf in raw_custom.get(group, []):
            cf_key = cf.get("key", "")
            cf_label = cf.get("label", "")
            if cf_key and cf_label:
                key_to_label[cf_key] = cf_label

        for key, val in group_data.items():
            if key.startswith("_"):
                continue

            # 新形式: {"label": "...", "value": "..."} で保存されている場合
            if isinstance(val, dict) and "label" in val and "value" in val:
                label = val["label"]
                actual_val = val["value"]
                if actual_val and str(actual_val).strip():
                    result[label] = str(actual_val).strip()
                continue

            # 旧形式: 文字列で保存されている場合
            if not val or not str(val).strip():
                continue
            label = key_to_label.get(key)
            if not label:
                if key.startswith("custom_"):
                    # グループをまたいで _custom_fields を検索
                    found_label = None
                    for g_customs in raw_custom.values():
                        if not isinstance(g_customs, list):
                            continue
                        for cf in g_customs:
                            if cf.get("key") == key:
                                found_label = cf.get("label")
                                break
                        if found_label:
                            break
                    if found_label:
                        label = found_label
                    else:
                        continue  # ラベルが見つからない場合はスキップ
                else:
                    label = key
            result[label] = str(val).strip()

    return result


def load_profile_fields() -> dict:
    """グループ別フィールド定義（カスタム含む）を返す。"""
    profile = load_profile()
    custom_fields = profile.get("_custom_fields", {})
    if isinstance(custom_fields, list):
        custom_fields = {}
    result = {}
    for group, fields in PROFILE_GROUP_FIELDS.items():
        customs = custom_fields.get(group, [])
        if not isinstance(customs, list):
            customs = []
        result[group] = list(fields) + [(f["key"], f["label"], "") for f in customs]
    return result


def save_profile_custom_field(group: str, key: str, label: str) -> None:
    profile = load_profile()
    customs = profile.get("_custom_fields", {})
    if isinstance(customs, list):
        customs = {}
    group_customs = customs.get(group, [])
    if not isinstance(group_customs, list):
        group_customs = []
    if not any(f["key"] == key for f in group_customs):
        group_customs.append({"key": key, "label": label})
    customs[group] = group_customs
    profile["_custom_fields"] = customs
    save_profile(profile)


def delete_profile_custom_field(group: str, key: str) -> None:
    profile = load_profile()
    customs = profile.get("_custom_fields", {})
    if isinstance(customs, list):
        customs = {}
    group_customs = customs.get(group, [])
    if isinstance(group_customs, list):
        customs[group] = [f for f in group_customs if f["key"] != key]
    if group in profile and isinstance(profile[group], dict):
        profile[group].pop(key, None)
    profile["_custom_fields"] = customs
    save_profile(profile)
