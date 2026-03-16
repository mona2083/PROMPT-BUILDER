# storage.py

import json
import os
from datetime import datetime
from typing import Any

HISTORY_FILE   = "history.json"
FAVORITES_FILE = "favorites.json"
SETTINGS_FILE  = "settings.json"

# ────────────────────────────────────────────
# 共通ユーティリティ
# ────────────────────────────────────────────
def _load(filepath: str) -> list | dict:
    if not os.path.exists(filepath):
        return [] if filepath != SETTINGS_FILE else {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(filepath: str, data: Any) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ────────────────────────────────────────────
# 履歴
# ────────────────────────────────────────────
def save_history(category: str, lang: str, prompt: str, answer: str) -> None:
    """Q&Aを履歴に追加する。最大100件保持。"""
    history = _load(HISTORY_FILE)
    history.insert(0, {
        "id":        datetime.now().strftime("%Y%m%d_%H%M%S"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category":  category,
        "lang":      lang,
        "prompt":    prompt,
        "answer":    answer,
    })
    _save(HISTORY_FILE, history[:100])

def load_history() -> list:
    return _load(HISTORY_FILE)

def delete_history(entry_id: str) -> None:
    history = [h for h in _load(HISTORY_FILE) if h["id"] != entry_id]
    _save(HISTORY_FILE, history)

def clear_history() -> None:
    _save(HISTORY_FILE, [])

# ────────────────────────────────────────────
# お気に入り
# ────────────────────────────────────────────
def save_favorite(category: str, lang: str, prompt: str, title: str = "") -> None:
    """プロンプトをお気に入りに追加する。最大50件保持。"""
    favorites = _load(FAVORITES_FILE)
    favorites.insert(0, {
        "id":        datetime.now().strftime("%Y%m%d_%H%M%S"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category":  category,
        "lang":      lang,
        "title":     title or prompt[:40] + "...",
        "prompt":    prompt,
    })
    _save(FAVORITES_FILE, favorites[:50])

def load_favorites() -> list:
    return _load(FAVORITES_FILE)

def delete_favorite(entry_id: str) -> None:
    favorites = [f for f in _load(FAVORITES_FILE) if f["id"] != entry_id]
    _save(FAVORITES_FILE, favorites)

# ────────────────────────────────────────────
# 設定
# ────────────────────────────────────────────
DEFAULT_SETTINGS = {
    "api_key":      "",
    "model":        "gemini-2.5-flash",
    "send_to_api":  True,
}

def load_settings() -> dict:
    settings = _load(SETTINGS_FILE)
    # デフォルト値で不足キーを補完
    for k, v in DEFAULT_SETTINGS.items():
        if k not in settings:
            settings[k] = v
    return settings

def save_settings(settings: dict) -> None:
    _save(SETTINGS_FILE, settings)

# ────────────────────────────────────────────
# プリセット
# ────────────────────────────────────────────
PRESETS_FILE = "presets.json"

def load_presets(category: str) -> list:
    """カテゴリのプリセット一覧を返す。"""
    all_presets = _load(PRESETS_FILE) if os.path.exists(PRESETS_FILE) else {}
    return all_presets.get(category, [])

def save_preset(category: str, name: str, fields: dict) -> None:
    """プリセットを保存する。同名があれば上書き。"""
    all_presets = _load(PRESETS_FILE) if os.path.exists(PRESETS_FILE) else {}
    if category not in all_presets:
        all_presets[category] = []
    # 同名があれば上書き
    all_presets[category] = [
        p for p in all_presets[category] if p["name"] != name
    ]
    all_presets[category].insert(0, {
        "id":     datetime.now().strftime("%Y%m%d_%H%M%S"),
        "name":   name,
        "fields": fields,
    })
    _save(PRESETS_FILE, all_presets)

def delete_preset(category: str, preset_id: str) -> None:
    """プリセットを削除する。"""
    all_presets = _load(PRESETS_FILE) if os.path.exists(PRESETS_FILE) else {}
    if category in all_presets:
        all_presets[category] = [
            p for p in all_presets[category] if p["id"] != preset_id
        ]
    _save(PRESETS_FILE, all_presets)

# ────────────────────────────────────────────
# グループ別プロフィール
# ────────────────────────────────────────────
PROFILE_FILE = "profile.json"

# カテゴリ → プロフィールグループのマッピング
CATEGORY_PROFILE_MAP = {
    "ai_pm":    ["common", "tech"],
    "code":     ["common", "tech"],
    "health":   ["common", "life"],
    "recipe":   ["common", "recipe"],   # ← lifeからrecipeに変更
    "study":    ["common", "study"],
    "language": ["common", "study"],
    "chat":     ["common"],
    "other":    ["common"],
}

# グループ別デフォルトフィールド定義
# (field_key, label, placeholder)
PROFILE_GROUP_FIELDS = {
    "common": [
        ("name",         {"ja": "名前 / 呼び方",       "en": "Name"},          {"ja": "", "en": ""}),
        ("age",          {"ja": "年齢・ライフステージ", "en": "Age / Stage"},   {"ja": "例: 30代・社会人", "en": "e.g. 30s, working professional"}),
        ("occupation",   {"ja": "職業・役職",           "en": "Occupation"},    {"ja": "例: AIエンジニア・PM", "en": "e.g. AI Engineer, PM"}),
        ("native_lang",  {"ja": "母語 / 日常使用言語",  "en": "Native Language"},{"ja": "例: 日本語", "en": "e.g. Japanese"}),
        ("answer_style", {"ja": "回答スタイルの好み",   "en": "Preferred Style"},{"ja": "例: 箇条書きで簡潔に", "en": "e.g. Concise bullet points"}),
        ("other",        {"ja": "その他・備考",         "en": "Notes"},         {"ja": "例: 基本的に丁寧語で", "en": "e.g. Keep it formal"}),
    ],
    "tech": [
        ("os",           {"ja": "作業環境（OS）",       "en": "OS / Environment"},{"ja": "例: macOS 14 / Apple Silicon", "en": "e.g. macOS 14 / Apple Silicon"}),
        ("main_lang",    {"ja": "主な使用言語",         "en": "Main Languages"}, {"ja": "例: Python・TypeScript", "en": "e.g. Python, TypeScript"}),
        ("experience",   {"ja": "経験職種と年数",       "en": "Experience"},     {"ja": "例: バックエンド5年 / ML2年", "en": "e.g. Backend 5yr / ML 2yr"}),
        ("dev_env",      {"ja": "メイン開発環境",       "en": "Dev Environment"},{"ja": "例: VSCode / Docker / GitHub", "en": "e.g. VSCode / Docker / GitHub"}),
        ("tech_rules",   {"ja": "最低要求・ルール",     "en": "Rules / Requirements"},{"ja": "例: コードは依頼するまで書かないで", "en": "e.g. Don't write code unless asked"}),
        ("tech_level",   {"ja": "技術レベル",           "en": "Tech Level"},     {"ja": "例: 中級・本番経験あり", "en": "e.g. Intermediate, production exp."}),
    ],
    "life": [
        ("lifestyle",    {"ja": "生活スタイル",           "en": "Lifestyle"},       {"ja": "例: 在宅勤務・一人暮らし",    "en": "e.g. Remote work, living alone"}),
        ("hobbies",      {"ja": "趣味・好きなこと",         "en": "Hobbies"},         {"ja": "例: 料理・ヨガ・読書",        "en": "e.g. Cooking, yoga, reading"}),
        ("personality",  {"ja": "性格",                   "en": "Personality"},      {"ja": "例: 几帳面・計画的",          "en": "e.g. Detail-oriented, organized"}),
        ("health_notes", {"ja": "健康目標・気をつけていること", "en": "Health Goals"}, {"ja": "例: 塩分控えめ・週3運動",    "en": "e.g. Low sodium, exercise 3x/week"}),
        ("household",    {"ja": "家族構成・人数",            "en": "Household"},       {"ja": "例: 1人暮らし",              "en": "e.g. Living alone"}),
    ],
    "recipe": [
        ("living_env",    {"ja": "生活環境・居住地",         "en": "Living Environment"}, {"ja": "例: ハワイ在住・アジア系スーパーあり・Whole Foods近く", "en": "e.g. Hawaii, Asian grocery nearby, Whole Foods close"}),
        ("food_likes",    {"ja": "好きな料理・食の好み",      "en": "Food Likes"},         {"ja": "例: 日本食・スパイシー好き・あっさり系", "en": "e.g. Japanese food, spicy, light flavors"}),
        ("food_dislikes", {"ja": "苦手な食材・避けたいもの",  "en": "Food Dislikes"},      {"ja": "例: 甘いもの全般・牛乳（豆乳はOK）・パクチー", "en": "e.g. Sweets, dairy milk (soy milk OK), cilantro"}),
        ("allergies",     {"ja": "アレルギー・食事制限",      "en": "Allergies"},          {"ja": "例: なし / 乳製品アレルギー", "en": "e.g. None / Dairy allergy"}),
        ("staple_pantry", {"ja": "常備調味料",               "en": "Pantry Staples"},     {"ja": "例: 醤油・みりん・オリーブオイル・ナンプラー", "en": "e.g. Soy sauce, mirin, olive oil, fish sauce"}),
        ("staple_food",   {"ja": "常備食材",                 "en": "Staple Ingredients"}, {"ja": "例: 卵・玉ねぎ・にんにく・米", "en": "e.g. Eggs, onion, garlic, rice"}),
        ("kitchen_tools", {"ja": "持っている調理器具",        "en": "Kitchen Tools"},      {"ja": "例: フライパン・炊飯器・オーブン・圧力鍋", "en": "e.g. Frying pan, rice cooker, oven, pressure cooker"}),
    ],
    "study": [
        ("major",        {"ja": "専攻・学部",           "en": "Major / Dept."},  {"ja": "例: 経済学部2年", "en": "e.g. Economics, Year 2"}),
        ("study_level",  {"ja": "現在の学習レベル",     "en": "Current Level"},  {"ja": "例: 統計基礎は理解済み", "en": "e.g. Basics of statistics done"}),
        ("study_style",  {"ja": "学習スタイルの好み",   "en": "Learning Style"}, {"ja": "例: 具体例から入ってほしい", "en": "e.g. Start with examples"}),
        ("target_lang",  {"ja": "学習中の言語",         "en": "Target Language"},{"ja": "例: 英語・スペイン語", "en": "e.g. English, Spanish"}),
        ("lang_level",   {"ja": "語学レベル",           "en": "Language Level"}, {"ja": "例: TOEIC700・日常会話可", "en": "e.g. TOEIC 700, conversational"}),
        ("study_goal",   {"ja": "学習目標",             "en": "Study Goal"},     {"ja": "例: 来年IELTS7.0取得", "en": "e.g. IELTS 7.0 next year"}),
        ("study_rules",  {"ja": "学習のルール・希望",   "en": "Study Rules"},    {"ja": "例: 答えを直接教えないで", "en": "e.g. Don't give direct answers"}),
    ],
}

PROFILE_GROUP_LABELS = {
    "common": {"ja": "共通（全カテゴリ）",  "en": "Common (All)"},
    "tech":   {"ja": "PC・技術系",          "en": "Tech & Dev"},
    "life":   {"ja": "生活・健康",          "en": "Life & Health"},
    "recipe": {"ja": "料理・食事",          "en": "Cooking & Food"},
    "study":  {"ja": "学習系",              "en": "Study & Language"},
}


def migrate_profile(profile: dict) -> dict:
    """旧形式のカスタムフィールド値を新形式に変換する。"""
    raw_custom = profile.get("_custom_fields", {})
    if isinstance(raw_custom, list):
        raw_custom = {}

    changed = False
    for group, customs in raw_custom.items():
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
            label = key_to_label.get(key, key)
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
        result[group] = list(fields) + [(f["key"], f["label"], "") for f in customs]
    return result


def save_profile_custom_field(group: str, key: str, label: str) -> None:
    profile = load_profile()
    customs = profile.get("_custom_fields", {})
    group_customs = customs.get(group, [])
    if not any(f["key"] == key for f in group_customs):
        group_customs.append({"key": key, "label": label})
    customs[group] = group_customs
    profile["_custom_fields"] = customs
    save_profile(profile)


def delete_profile_custom_field(group: str, key: str) -> None:
    profile = load_profile()
    customs = profile.get("_custom_fields", {})
    group_customs = customs.get(group, [])
    customs[group] = [f for f in group_customs if f["key"] != key]
    if group in profile:
        profile[group].pop(key, None)
    profile["_custom_fields"] = customs
    save_profile(profile)

# ────────────────────────────────────────────
# フィールドオプション（プルダウン用カスタム値）
# ────────────────────────────────────────────
FIELD_OPTIONS_FILE = "field_options.json"

def load_field_options(category: str, field_key: str) -> list:
    """カテゴリ・フィールドのカスタムオプション一覧を返す。"""
    if not os.path.exists(FIELD_OPTIONS_FILE):
        return []
    with open(FIELD_OPTIONS_FILE, "r", encoding="utf-8") as f:
        all_opts = json.load(f)
    return all_opts.get(f"{category}_{field_key}", [])

def save_field_option(category: str, field_key: str, value: str) -> None:
    """カスタムオプションを追加する。重複は無視。"""
    if not os.path.exists(FIELD_OPTIONS_FILE):
        all_opts = {}
    else:
        with open(FIELD_OPTIONS_FILE, "r", encoding="utf-8") as f:
            all_opts = json.load(f)
    key = f"{category}_{field_key}"
    opts = all_opts.get(key, [])
    if value and value not in opts:
        opts.insert(0, value)
        all_opts[key] = opts[:50]
    _save(FIELD_OPTIONS_FILE, all_opts)

def delete_field_option(category: str, field_key: str, value: str) -> None:
    """カスタムオプションを削除する。"""
    if not os.path.exists(FIELD_OPTIONS_FILE):
        return
    with open(FIELD_OPTIONS_FILE, "r", encoding="utf-8") as f:
        all_opts = json.load(f)
    key = f"{category}_{field_key}"
    all_opts[key] = [v for v in all_opts.get(key, []) if v != value]
    _save(FIELD_OPTIONS_FILE, all_opts)

def load_all_field_options(category: str) -> dict:
    """カテゴリの全フィールドオプションを返す。"""
    if not os.path.exists(FIELD_OPTIONS_FILE):
        return {}
    with open(FIELD_OPTIONS_FILE, "r", encoding="utf-8") as f:
        all_opts = json.load(f)
    result = {}
    for k, v in all_opts.items():
        if k.startswith(f"{category}_"):
            field_key = k[len(category)+1:]
            result[field_key] = v
    return result

# ────────────────────────────────────────────
# AIへの指示プリセット
# ────────────────────────────────────────────
INSTRUCTIONS_FILE = "instructions.json"

DEFAULT_INSTRUCTION_PRESETS = {
    "general": {
        "name": {"ja": "基本ルール（汎用）", "en": "General Rules"},
        "instructions": [
            {"ja": "できるだけ簡潔に答えてください。聞いたことだけ答えてください。「もっと詳しく」「詳細は？」などと言わない限り余分な情報は不要です。", "en": "Answer as concisely as possible. Only answer what I asked — unless I say 'more details' or 'elaborate.'"},
            {"ja": "「素晴らしい質問ですね！」「もちろんです！」などの前置きは不要です。直接答えてください。", "en": "Don't add unnecessary preamble like 'Great question!' or 'Certainly!' Just answer directly."},
            {"ja": "不確かな情報や古い情報がある場合は必ず教えてください。", "en": "Always tell me if you're not sure about something, or if the information might be outdated."},
            {"ja": "知らない場合は知らないと言ってください。情報を作り上げないでください。", "en": "Don't make up information. If you don't know, just say so."},
            {"ja": "質問の解釈が複数ある場合は、答える前に確認してください。", "en": "If there are multiple interpretations of my question, ask for clarification before answering."},
            {"ja": "事実と意見・推測を明確に区別してください。", "en": "Distinguish clearly between facts and your opinions/assumptions."},
        ]
    },
    "accuracy": {
        "name": {"ja": "精度・信頼性重視", "en": "Accuracy & Reliability"},
        "instructions": [
            {"ja": "最新の情報を使用してください。", "en": "Please use the latest information available."},
            {"ja": "ファクトチェックを行い、情報の出典を教えてください。", "en": "Always fact-check and provide sources where you got the information."},
            {"ja": "不確かな情報や古い情報がある場合は必ず教えてください。", "en": "Always tell me if you're not sure about something, or if the information might be outdated."},
            {"ja": "知らない場合は知らないと言ってください。情報を作り上げないでください。", "en": "Don't make up information. If you don't know, just say so."},
            {"ja": "事実と意見・推測を明確に区別してください。", "en": "Distinguish clearly between facts and your opinions/assumptions."},
            {"ja": "質問の解釈が複数ある場合は、答える前に確認してください。", "en": "If there are multiple interpretations of my question, ask for clarification before answering."},
        ]
    },
    "reasoning": {
        "name": {"ja": "思考・推論プロセス重視", "en": "Reasoning & Thinking"},
        "instructions": [
            {"ja": "最終的な答えを出す前にステップバイステップで考えてください。", "en": "Think step by step before giving your final answer."},
            {"ja": "結論だけでなく、推論プロセスも見せてください。", "en": "Show your reasoning process, not just the conclusion."},
            {"ja": "仮定を置く場合は、最初に明示してください。", "en": "If you're making assumptions, state them explicitly upfront."},
            {"ja": "ハッピーパスだけでなく、エッジケースや例外も考慮してください。", "en": "Consider edge cases and exceptions, not just the happy path."},
            {"ja": "私のプランで問題が起きそうな点を教えてください。", "en": "Play devil's advocate — tell me what could go wrong with my plan."},
            {"ja": "私が間違っている場合は、上から目線にならずに直接指摘してください。", "en": "If I make a mistake, correct me directly without being condescending."},
            {"ja": "私のアプローチに反対意見がある場合は遠慮なく言ってください。検証ではなく正直な意見が欲しいです。", "en": "Push back if you disagree with my approach — I want your honest opinion, not just validation."},
        ]
    },
    "code": {
        "name": {"ja": "コード作業用", "en": "Code Tasks"},
        "instructions": [
            {"ja": "明示的に依頼しない限りコードを書かないでください。", "en": "Don't write code unless I explicitly ask for it."},
            {"ja": "コードを示す際は、何をどう変えたか・なぜ変えたかを説明してください。ファイル全体をそのまま貼り付けないでください。", "en": "When showing code, always explain what changed and why — don't just dump the whole file."},
            {"ja": "頼まれなくてもバグやエッジケースを指摘してください。", "en": "Point out potential bugs or edge cases even if I didn't ask."},
            {"ja": "より良い方法がある場合は簡単に触れてください。ただし、まず依頼されたことをやってください。", "en": "If my approach has a better alternative, mention it briefly — but still do what I asked first."},
            {"ja": "参照するファイル名と行番号を必ず明示してください。", "en": "Always specify which file and line number you're referring to."},
            {"ja": "私が言ったことを繰り返してから答えないでください。", "en": "Don't repeat what I just said before answering."},
        ]
    },
    "language": {
        "name": {"ja": "語学学習用", "en": "Language Learning"},
        "instructions": [
            {"ja": "文法の間違いは会話の流れを遮らず、返答の中で自然に修正してください。", "en": "Correct my grammar naturally within your reply, don't interrupt the flow to lecture me."},
            {"ja": "特に指示がない限り、私の現在の語彙レベルに合わせた言葉を使ってください。", "en": "Use words within my current vocabulary level unless I ask to stretch."},
            {"ja": "学習対象の言語で常に返答してください。", "en": "Always respond in the target language I'm learning, not in Japanese."},
            {"ja": "文法ミスがあれば返答の末尾に修正版を示してください。", "en": "If I make a grammar mistake, show the corrected version at the end of your reply."},
        ]
    },
    "format": {
        "name": {"ja": "出力フォーマット重視", "en": "Output Format"},
        "instructions": [
            {"ja": "私が使用した言語と同じ言語で返答してください。", "en": "Always respond in the same language I used to ask the question."},
            {"ja": "そのままコピー＆ペーストできる形式でフォーマットしてください。", "en": "Format your response so I can copy-paste it directly without editing."},
            {"ja": "複数の選択肢を挙げる際は、推奨順に並べてください。", "en": "When giving a list of options, rank them by what you recommend most."},
            {"ja": "長い返答の冒頭にはTL;DRを入れてください。", "en": "Always include a TL;DR at the top for long responses."},
            {"ja": "箇条書きはリストを列挙する場合のみ使用してください。説明には使わないでください。", "en": "Use bullet points only when listing things. Don't use them for explanations."},
            {"ja": "特に指示がない限り太字を使わないでください。", "en": "Never use bold text unless I specifically ask for it."},
            {"ja": "最後に要約しないでください。書いた内容は読めばわかります。", "en": "Don't summarize at the end. I can read what you wrote."},
        ]
    },
}


def load_instruction_presets() -> dict:
    if not os.path.exists(INSTRUCTIONS_FILE):
        return DEFAULT_INSTRUCTION_PRESETS.copy()
    with open(INSTRUCTIONS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    result = DEFAULT_INSTRUCTION_PRESETS.copy()
    result.update(data.get("custom", {}))
    return result


def save_instruction_preset(key: str, name: str, instructions: list) -> None:
    if not os.path.exists(INSTRUCTIONS_FILE):
        data = {"custom": {}}
    else:
        with open(INSTRUCTIONS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    if "custom" not in data:
        data["custom"] = {}
    data["custom"][key] = {"name": name, "instructions": instructions}
    _save(INSTRUCTIONS_FILE, data)


def delete_instruction_preset(key: str) -> None:
    if key in DEFAULT_INSTRUCTION_PRESETS:
        return
    if not os.path.exists(INSTRUCTIONS_FILE):
        return
    with open(INSTRUCTIONS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.get("custom", {}).pop(key, None)
    _save(INSTRUCTIONS_FILE, data)