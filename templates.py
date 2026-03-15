# templates.py

# ────────────────────────────────────────────
# UI テキスト（JA / EN 切り替え用）
# ────────────────────────────────────────────
LANG_UI = {
    "ja": {
        "title":            "AIプロンプトビルダー",
        "category_label":   "カテゴリを選択",
        "send_btn":         "送信",
        "copy_prompt_btn":  "プロンプトをコピー",
        "copy_answer_btn":  "回答をコピー",
        "clear_btn":        "クリア",
        "prompt_preview":   "▼ 生成されたプロンプト",
        "answer_label":     "▼ AIの回答",
        "loading":          "AIに送信中...",
        "error_api":        "APIキーを設定してください",
        "error_empty":      "必須項目を入力してください",
        "copied":           "コピーしました",
        "lang_toggle":      "EN",
    },
    "en": {
        "title":            "AI Prompt Builder",
        "category_label":   "Select Category",
        "send_btn":         "Send",
        "copy_prompt_btn":  "Copy Prompt",
        "copy_answer_btn":  "Copy Answer",
        "clear_btn":        "Clear",
        "prompt_preview":   "▼ Generated Prompt",
        "answer_label":     "▼ AI Answer",
        "loading":          "Sending to AI...",
        "error_api":        "Please set your API key",
        "error_empty":      "Please fill in required fields",
        "copied":           "Copied",
        "lang_toggle":      "JA",
    },
}

# ────────────────────────────────────────────
# カテゴリ名
# ────────────────────────────────────────────
CATEGORIES = {
    "ja": ["AI-PM", "コード", "生活・健康", "大学勉強", "語学学習", "チャット", "レシピ", "その他"],
    "en": ["AI-PM", "Code", "Health & Life", "Study", "Language", "Chat", "Recipe", "Other"],
}

CATEGORY_KEY_MAP = {
    "AI-PM":         "ai_pm",
    "コード":         "code",
    "Code":          "code",
    "生活・健康":     "health",
    "Health & Life": "health",
    "大学勉強":       "study",
    "Study":         "study",
    "語学学習":       "language",
    "Language":      "language",
    "チャット":       "chat",
    "Chat":          "chat",
    "レシピ":         "recipe",
    "Recipe":        "recipe",
    "その他":         "other",
    "Other":         "other",
}

# ────────────────────────────────────────────
# テンプレート定義
# fields の各タプル:
#   (field_key, label, placeholder, required, options)
#   options: プルダウン候補リスト（空リストの場合はテキスト入力のみ）
# ────────────────────────────────────────────
TEMPLATES = {

    # ── AI-PM ──────────────────────────────────────────────────────
    "ai_pm": {
        "ja": {
            "role": (
                "あなたはAI開発プロジェクトの経験豊富なシニアプロジェクトマネージャーです。"
                "リスク管理・意思決定・ステークホルダーマネジメントを得意としています。"
            ),
            "fields": [
                ("phase", "フェーズ", "例: 評価フェーズ完了後", False, [
                    "要件定義フェーズ", "データ収集・整備フェーズ", "モデル開発フェーズ",
                    "評価フェーズ", "評価フェーズ完了後", "本番移行直前",
                    "本番稼働中", "運用・保守フェーズ", "改善・再学習フェーズ",
                ]),
                ("team", "チーム規模", "例: エンジニア4名 / DS2名 / PM1名", False, [
                    "エンジニア1名（個人）", "エンジニア2〜3名", "エンジニア4〜6名 / DS2名 / PM1名",
                    "エンジニア10名以上 / DS5名 / PM2名", "大規模チーム（50名以上）",
                    "外部委託含む混成チーム",
                ]),
                ("stakeholders", "ステークホルダー", "例: 事業部長・法務", False, [
                    "事業部長", "経営層・役員", "法務・コンプライアンス",
                    "インフラ・セキュリティチーム", "営業・マーケティング",
                    "カスタマーサポート", "外部パートナー・ベンダー", "規制当局",
                ]),
                ("question", "質問・課題", "例: リリース判断の基準を教えてください", True, []),
                ("output_expectation", "期待する出力", "例: 選択肢A/B/Cの比較・推奨案", False, [
                    "選択肢A/B/Cの比較表", "推奨案と理由（1段落）",
                    "リスク一覧（発生確率・影響度・対策）", "ロードマップ（マイルストーン付き）",
                    "ステータスレポート形式", "ポストモーテム形式", "RACI表",
                ]),
            ],
            "rules": [
                "リスクは「技術・組織・倫理・ビジネス」の4軸で評価してください。",
                "意思決定は選択肢A/B/Cの形式で、各メリット・デメリット・推奨条件を含めてください。",
                "AIプロジェクト固有のリスク（モデルドリフト・データ品質・説明責任）も考慮してください。",
            ],
            "output_format": (
                "以下の形式で出力してください：\n"
                "## 状況整理\n## 選択肢（A/B/C）\n## 推奨案と理由\n## 注意点・リスク"
            ),
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a senior project manager with extensive experience in AI development projects. "
                "You specialize in risk management, decision-making, and stakeholder management."
            ),
            "fields": [
                ("phase", "Phase", "e.g. Post-evaluation, pre-production", False, [
                    "Requirements definition", "Data collection & preparation",
                    "Model development", "Evaluation phase", "Post-evaluation",
                    "Pre-production", "Production", "Operations & maintenance",
                ]),
                ("team", "Team size", "e.g. 4 engineers / 2 DS / 1 PM", False, [
                    "Solo (1 person)", "Small (2-3 engineers)",
                    "Medium (4-6 eng / 2 DS / 1 PM)", "Large (10+ eng / 5 DS / 2 PM)",
                    "Enterprise (50+)", "Mixed with external vendors",
                ]),
                ("stakeholders", "Stakeholders", "e.g. Division head, Legal", False, [
                    "Division head", "C-suite / Executives", "Legal & Compliance",
                    "Infrastructure / Security", "Sales & Marketing",
                    "Customer support", "External partners / Vendors", "Regulators",
                ]),
                ("question", "Question / Issue", "e.g. What criteria should we use to ship?", True, []),
                ("output_expectation", "Expected output", "e.g. Options A/B/C comparison", False, [
                    "Options A/B/C comparison table", "Recommendation with rationale",
                    "Risk register (likelihood/impact/mitigation)", "Roadmap with milestones",
                    "Status report format", "Post-mortem format", "RACI chart",
                ]),
            ],
            "rules": [
                "Evaluate risks across 4 axes: Technical, Organizational, Ethical, Business.",
                "Present decisions as options A/B/C with pros, cons, and recommended conditions.",
                "Consider AI-specific risks: model drift, data quality, explainability.",
            ],
            "output_format": (
                "Output in this format:\n"
                "## Situation Summary\n## Options (A/B/C)\n## Recommendation & Rationale\n## Risks & Caveats"
            ),
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Code ───────────────────────────────────────────────────────
    "code": {
        "ja": {
            "role": (
                "あなたはMLエンジニアリングの経験豊富なシニアエンジニアです。"
                "クリーンコード・型安全・再現性を重視したコードを書きます。"
            ),
            "fields": [
                ("env", "実行環境", "例: macOS / Python 3.11 / torch==2.3", False, [
                    "macOS / Python 3.11 / CPU",
                    "macOS / Python 3.11 / MPS (Apple Silicon)",
                    "Linux / Python 3.11 / CUDA",
                    "Windows / Python 3.10 / CPU",
                    "Google Colab / Python 3.10 / GPU",
                    "Docker / Python 3.11",
                    "Jupyter Notebook",
                ]),
                ("purpose", "目的（1文）", "例: BERTで文章をベクトル化する関数を作りたい", False, []),
                ("input", "入力の型・形状", "例: List[str]、最大512トークン", False, [
                    "List[str]", "np.ndarray shape=(N,)",
                    "np.ndarray shape=(N, D)", "torch.Tensor shape=(B, T)",
                    "pd.DataFrame", "dict", "JSON文字列", "画像ファイルパス",
                ]),
                ("quality", "品質基準", "例: 型ヒント・docstring付き", False, [
                    "型ヒント（Type hints）付き",
                    "docstring（Google形式）付き",
                    "型ヒント＋docstring付き",
                    "pytestテストコード付き",
                    "型ヒント＋docstring＋pytest付き",
                    "本番品質（全て込み）",
                    "プロトタイプ（動けばOK）",
                ]),
                ("error", "エラーメッセージ", "エラーが出ている場合は全文貼り付け", False, []),
                ("question", "質問・依頼内容", "例: 上記の実装コードを書いてください", True, []),
                ("output_expectation", "期待する出力", "例: 関数1つ・型ヒント付き", False, [
                    "関数1つ（型ヒント付き）",
                    "クラス実装",
                    "関数＋テストコード",
                    "実装＋使用例＋テスト",
                    "デバッグ済みコード＋原因説明",
                    "コードレビュー＋改善案",
                    "リファクタリング済みコード",
                ]),
            ],
            "rules": [
                "型ヒント（Type hints）を全関数に付けてください。",
                "docstringはGoogle形式で書いてください。",
                "乱数シード・device自動判定（cuda/mps/cpu）を必ず含めてください。",
                "コメントは「なぜそうしているか（Why）」に限定してください。",
            ],
            "output_format": (
                "以下の順で出力してください：\n"
                "1. 実装コード（コードブロック）\n2. 使用例\n"
                "3. テストコード（pytest形式）\n4. 注意点・改善案"
            ),
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a senior ML engineer with deep expertise in production-ready AI systems. "
                "You prioritize clean code, type safety, and reproducibility."
            ),
            "fields": [
                ("env", "Environment", "e.g. macOS / Python 3.11 / MPS", False, [
                    "macOS / Python 3.11 / CPU",
                    "macOS / Python 3.11 / MPS (Apple Silicon)",
                    "Linux / Python 3.11 / CUDA",
                    "Windows / Python 3.10 / CPU",
                    "Google Colab / Python 3.10 / GPU",
                    "Docker / Python 3.11",
                    "Jupyter Notebook",
                ]),
                ("purpose", "Purpose in 1 line", "e.g. Vectorize sentences using BERT", False, []),
                ("input", "Input type & shape", "e.g. List[str], max 512 tokens", False, [
                    "List[str]", "np.ndarray shape=(N,)",
                    "np.ndarray shape=(N, D)", "torch.Tensor shape=(B, T)",
                    "pd.DataFrame", "dict", "JSON string", "Image file path",
                ]),
                ("quality", "Quality standard", "e.g. Type hints + docstring", False, [
                    "Type hints only",
                    "Docstring (Google style) only",
                    "Type hints + docstring",
                    "With pytest test cases",
                    "Type hints + docstring + pytest",
                    "Production quality (all included)",
                    "Prototype (just make it work)",
                ]),
                ("error", "Error message", "Paste full error message if applicable", False, []),
                ("question", "Question / Request", "e.g. Please write the implementation", True, []),
                ("output_expectation", "Expected output", "e.g. Single function with type hints", False, [
                    "Single function (with type hints)",
                    "Class implementation",
                    "Function + test code",
                    "Implementation + usage example + tests",
                    "Debugged code + explanation",
                    "Code review + improvements",
                    "Refactored code",
                ]),
            ],
            "rules": [
                "Add type hints to all functions.",
                "Write docstrings in Google style.",
                "Always include random seed fixing and device auto-detection (cuda/mps/cpu).",
                "Limit comments to 'Why', not 'What'.",
            ],
            "output_format": (
                "Output in this order:\n"
                "1. Implementation code (code block)\n2. Usage example\n"
                "3. Test code (pytest style)\n4. Notes & improvements"
            ),
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Health & Life ──────────────────────────────────────────────
    "health": {
        "ja": {
            "role": (
                "あなたは栄養学と健康管理に精通したアドバイザーです。"
                "科学的根拠に基づいた、実践しやすい提案を行います。"
            ),
            "fields": [
                ("profile", "プロフィール", "例: 30代男性・在宅勤務", False, [
                    "20代女性・オフィス勤務", "20代男性・オフィス勤務",
                    "30代女性・在宅勤務", "30代男性・在宅勤務",
                    "40代女性・立ち仕事", "40代男性・立ち仕事",
                    "50代・デスクワーク中心", "学生・運動習慣あり",
                ]),
                ("goal", "目標", "例: 3ヶ月で3kg減量", False, [
                    "体重を減らしたい（ゆっくり）", "体重を減らしたい（短期集中）",
                    "筋肉をつけたい", "体力・持久力をつけたい",
                    "食生活を改善したい", "睡眠の質を上げたい",
                    "ストレスを減らしたい", "免疫力を上げたい",
                    "血糖値・血圧を改善したい",
                ]),
                ("constraints", "制約・アレルギー", "例: 甲殻類アレルギー・調理20分以内", False, [
                    "アレルギーなし", "甲殻類アレルギー", "乳製品アレルギー",
                    "卵アレルギー", "小麦アレルギー（グルテンフリー）",
                    "調理時間15分以内", "調理時間30分以内",
                    "1食500円以内", "1食1000円以内",
                    "電子レンジのみ", "一人暮らし向け",
                ]),
                ("question", "質問・相談内容", "例: 昼食のおすすめを教えてください", True, []),
                ("output_expectation", "期待する出力", "例: レシピ形式・箇条書き3点", False, [
                    "レシピ形式（材料・手順・カロリー）",
                    "1週間の食事プラン",
                    "おすすめ食材リスト",
                    "箇条書き3点のアドバイス",
                    "運動メニュー提案",
                    "習慣改善のステップ",
                ]),
            ],
            "rules": [
                "提案には科学的・栄養学的根拠（1〜2文）を必ず含めてください。",
                "効果が出るまでの目安期間を明示してください。",
                "過度にやりすぎた場合のリスクも添えてください。",
                "医師や栄養士への相談が必要な点があれば明示してください。",
            ],
            "output_format": (
                "レシピの場合は以下の形式で出力してください：\n"
                "【材料】（人数分）\n【カロリー概算】\n【手順】（所要時間付き）\n"
                "【栄養バランスのポイント】\n【アレンジ提案】2パターン\n【保存期間】"
            ),
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a health and nutrition advisor with expertise in evidence-based wellness. "
                "You provide practical, science-backed recommendations."
            ),
            "fields": [
                ("profile", "Profile", "e.g. Male, 30s, remote work", False, [
                    "Female, 20s, office work", "Male, 20s, office work",
                    "Female, 30s, remote work", "Male, 30s, remote work",
                    "Female, 40s, standing job", "Male, 40s, standing job",
                    "50s, desk job", "Student, active lifestyle",
                ]),
                ("goal", "Goal", "e.g. Lose 3kg in 3 months", False, [
                    "Lose weight (gradual)", "Lose weight (fast)",
                    "Build muscle", "Improve endurance",
                    "Improve diet quality", "Better sleep",
                    "Reduce stress", "Boost immunity",
                    "Improve blood sugar / blood pressure",
                ]),
                ("constraints", "Constraints / Allergies", "e.g. Shellfish allergy", False, [
                    "No allergies", "Shellfish allergy", "Dairy allergy",
                    "Egg allergy", "Gluten-free", "Under 15 min cooking",
                    "Under 30 min cooking", "Under $5/meal", "Microwave only",
                ]),
                ("question", "Question", "e.g. Suggest a healthy lunch for me", True, []),
                ("output_expectation", "Expected output", "e.g. Recipe format", False, [
                    "Recipe format (ingredients, steps, calories)",
                    "1-week meal plan", "Recommended ingredients list",
                    "3 bullet-point tips", "Exercise plan", "Habit improvement steps",
                ]),
            ],
            "rules": [
                "Include scientific/nutritional rationale (1-2 sentences) for each recommendation.",
                "State the expected timeframe to see results.",
                "Mention risks of overdoing it.",
                "Flag any points that require consultation with a doctor or dietitian.",
            ],
            "output_format": (
                "For recipes, use this format:\n"
                "[Ingredients] (servings)\n[Estimated calories]\n[Steps] (with time per step)\n"
                "[Nutrition highlights]\n[2 variation ideas]\n[Storage duration]"
            ),
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Study ──────────────────────────────────────────────────────
    "study": {
        "ja": {
            "role": (
                "あなたは大学生の学習をサポートする経験豊富な家庭教師です。"
                "理解を深めることを最優先に、ソクラテス式の対話で丁寧に教えます。"
            ),
            "fields": [
                ("subject", "科目・分野", "例: 統計学（大学2年）", False, [
                    "統計学", "線形代数", "微積分",
                    "機械学習", "深層学習", "データサイエンス",
                    "プログラミング（Python）", "プログラミング（Java）",
                    "経済学・ミクロ経済", "経済学・マクロ経済",
                    "会計学", "法学（民法）", "英語学術ライティング",
                ]),
                ("major", "専攻・学年", "例: 経済学部2年", False, [
                    "理工学部 1年", "理工学部 2年", "理工学部 3年", "理工学部 4年",
                    "経済学部 1年", "経済学部 2年", "経済学部 3年", "経済学部 4年",
                    "文学部", "法学部", "医学部", "情報学部", "大学院生",
                ]),
                ("level", "現在の理解レベル", "例: 平均・分散は分かる。正規分布が曖昧", False, [
                    "全くの初心者", "基礎概念は理解済み", "教科書は読んだが演習が苦手",
                    "演習はできるが応用が難しい", "応用まで理解したい",
                    "試験前の総復習", "レポート・論文執筆中",
                ]),
                ("style", "希望する教え方", "例: 具体例から始めてほしい", False, [
                    "直感的な説明から入ってほしい",
                    "具体例から始めて徐々に抽象化",
                    "数式・定義から入ってほしい",
                    "ソクラテス式（質問で導いてほしい）",
                    "間違いやすいポイントを重点的に",
                    "試験対策・頻出問題中心に",
                ]),
                ("question", "質問内容", "例: 中心極限定理を理解したい", True, []),
                ("output_expectation", "期待する出力", "例: 直感的な説明＋確認問題2問", False, [
                    "直感的な説明のみ",
                    "直感的な説明＋数式",
                    "直感的な説明＋数式＋確認問題2問",
                    "例題の解き方（ステップバイステップ）",
                    "よくある誤解の解説",
                    "試験対策サマリー",
                    "レポートのフィードバック",
                ]),
            ],
            "rules": [
                "まず直感的な説明を行い、その後数式・定義に進んでください。",
                "身近な具体例を必ず1つ以上含めてください。",
                "間違いやすいポイントと典型的な誤解を明示してください。",
                "答えを直接教えるのではなく、理解を確認しながら進めてください。",
            ],
            "output_format": (
                "以下の形式で出力してください：\n"
                "## 直感的な説明\n## 具体例\n## 正式な定義・数式\n"
                "## よくある誤解\n## 理解確認の小問（2問）\n## 次に学ぶべきトピック"
            ),
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are an experienced tutor supporting university students. "
                "You prioritize deep understanding using the Socratic method and concrete examples."
            ),
            "fields": [
                ("subject", "Subject", "e.g. Statistics (2nd year)", False, [
                    "Statistics", "Linear Algebra", "Calculus",
                    "Machine Learning", "Deep Learning", "Data Science",
                    "Python Programming", "Java Programming",
                    "Microeconomics", "Macroeconomics",
                    "Accounting", "Academic Writing",
                ]),
                ("major", "Major / Year", "e.g. Economics, Year 2", False, [
                    "Engineering Year 1", "Engineering Year 2",
                    "Engineering Year 3", "Engineering Year 4",
                    "Economics Year 1", "Economics Year 2",
                    "Economics Year 3", "Economics Year 4",
                    "Arts", "Law", "Medicine", "Computer Science", "Graduate student",
                ]),
                ("level", "Current understanding", "e.g. I know mean/variance but not normal dist.", False, [
                    "Complete beginner", "Understand basic concepts",
                    "Read the textbook but struggle with exercises",
                    "Can do exercises but struggle with applications",
                    "Want to master applications", "Pre-exam review",
                ]),
                ("style", "Teaching style", "e.g. Start with examples", False, [
                    "Start with intuition", "Examples first, then abstract",
                    "Formal definition first", "Socratic method",
                    "Focus on common mistakes", "Exam-focused practice",
                ]),
                ("question", "Question", "e.g. Help me understand the CLT", True, []),
                ("output_expectation", "Expected output", "e.g. Intuition + 2 quiz questions", False, [
                    "Intuitive explanation only",
                    "Intuition + formula",
                    "Intuition + formula + 2 quiz questions",
                    "Step-by-step problem solving",
                    "Common misconceptions explained",
                    "Exam prep summary",
                    "Report feedback",
                ]),
            ],
            "rules": [
                "Start with intuitive explanation, then move to formal definition.",
                "Always include at least one real-world example.",
                "Explicitly flag common mistakes and misconceptions.",
                "Guide understanding step by step rather than giving direct answers.",
            ],
            "output_format": (
                "Output in this format:\n"
                "## Intuitive Explanation\n## Concrete Example\n## Formal Definition\n"
                "## Common Misconceptions\n## Quick Check Questions (x2)\n## What to Study Next"
            ),
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Language / 語学学習 ────────────────────────────────────────
    "language": {
        "ja": {
            "role": (
                "あなたは経験豊富な語学教師です。"
                "学習者のレベルと目的に合わせて、実践的で効果的な語学学習をサポートします。"
            ),
            "fields": [
                ("target_lang", "学習言語", "例: 英語", False, [
                    "英語", "スペイン語", "イタリア語", "ポルトガル語",
                    "フランス語", "ドイツ語", "中国語（普通話）",
                    "韓国語", "アラビア語", "ロシア語", "日本語",
                ]),
                ("level", "現在のレベル", "例: TOEIC600点・日常会話程度", False, [
                    "完全な初心者（ゼロから）",
                    "初級（挨拶・簡単な表現ができる）",
                    "中級（日常会話ができる）",
                    "中上級（複雑な話題も話せる）",
                    "上級（ほぼネイティブ）",
                    "TOEIC 400〜500点", "TOEIC 600〜700点",
                    "TOEIC 800点以上", "IELTS 5.0〜6.0",
                    "IELTS 6.5以上", "英検2級", "英検準1級", "英検1級",
                ]),
                ("learning_type", "学習したい内容", "例: 会話練習", False, [
                    "会話練習（フリートーク）",
                    "ボキャブラリ強化",
                    "リスニング練習",
                    "ライティング・文章作成",
                    "リーディング読解",
                    "文法の整理・強化",
                    "発音矯正・フォネティクス",
                    "資格対策（TOEIC）",
                    "資格対策（IELTS）",
                    "資格対策（英検）",
                    "資格対策（TOEFL）",
                ]),
                ("field", "練習フィールド", "例: ビジネス・日常会話", False, [
                    "日常会話・雑談",
                    "ビジネス（メール・会議）",
                    "医療・ヘルスケア",
                    "IT・テクノロジー",
                    "職場・社内コミュニケーション",
                    "旅行・観光",
                    "学術・研究",
                    "ニュース・時事",
                    "エンターテイメント・映画・音楽",
                    "スポーツ",
                ]),
                ("question", "質問・依頼内容", "例: 今日のレッスンをお願いします", True, []),
                ("output_expectation", "期待する出力", "例: 例文5つ・会話形式", False, [
                    "例文5つ（日本語訳付き）",
                    "会話形式のダイアログ",
                    "単語リスト＋例文",
                    "文法解説＋練習問題",
                    "模範解答＋フィードバック",
                    "発音ガイド",
                    "模擬試験問題",
                ]),
            ],
            "rules": [
                "学習者のレベルに合わせた語彙・文法を使ってください。",
                "例文は必ず実際の場面で使える自然な表現にしてください。",
                "間違いやすいポイントや注意事項を明示してください。",
                "発音のポイントがある場合は補足してください。",
                "練習問題や確認テストを含めると効果的です。",
            ],
            "output_format": (
                "以下の形式で出力してください：\n"
                "## 今日のテーマ\n## 重要表現・単語（例文付き）\n"
                "## 練習問題\n## よくある間違いと注意点\n## 次のステップ"
            ),
            "lang_instruction": "解説は日本語で行い、学習対象言語の例文・表現は元の言語で記載してください。",
        },
        "en": {
            "role": (
                "You are an experienced language teacher. "
                "You provide practical and effective language learning support tailored to the learner's level and goals."
            ),
            "fields": [
                ("target_lang", "Target language", "e.g. Spanish", False, [
                    "Spanish", "Italian", "Portuguese",
                    "French", "German", "Mandarin Chinese",
                    "Korean", "Arabic", "Russian", "Japanese",
                ]),
                ("level", "Current level", "e.g. Intermediate / IELTS 6.0", False, [
                    "Complete beginner", "Beginner (basic greetings)",
                    "Elementary (simple conversations)", "Intermediate (daily conversations)",
                    "Upper-intermediate", "Advanced (near-native)",
                    "IELTS 5.0-6.0", "IELTS 6.5+", "TOEFL 80-100", "TOEFL 100+",
                ]),
                ("learning_type", "Learning focus", "e.g. Conversation practice", False, [
                    "Conversation practice (free talk)",
                    "Vocabulary building",
                    "Listening practice",
                    "Writing & composition",
                    "Reading comprehension",
                    "Grammar review",
                    "Pronunciation / Phonetics",
                    "Exam prep (IELTS)",
                    "Exam prep (TOEFL)",
                    "Exam prep (Cambridge)",
                ]),
                ("field", "Practice field", "e.g. Business, daily life", False, [
                    "Daily life / Small talk",
                    "Business (email, meetings)",
                    "Medical / Healthcare",
                    "IT / Technology",
                    "Workplace communication",
                    "Travel / Tourism",
                    "Academic / Research",
                    "News / Current events",
                    "Entertainment / Movies / Music",
                    "Sports",
                ]),
                ("question", "Question / Request", "e.g. Please start today's lesson", True, []),
                ("output_expectation", "Expected output", "e.g. 5 examples, dialogue format", False, [
                    "5 example sentences (with translation)",
                    "Dialogue format",
                    "Vocabulary list + examples",
                    "Grammar explanation + exercises",
                    "Model answer + feedback",
                    "Pronunciation guide",
                    "Practice test questions",
                ]),
            ],
            "rules": [
                "Use vocabulary and grammar appropriate to the learner's level.",
                "Example sentences must be natural and usable in real situations.",
                "Highlight common mistakes and points to watch out for.",
                "Include pronunciation tips when relevant.",
                "Add practice exercises or a short quiz when helpful.",
            ],
            "output_format": (
                "Output in this format:\n"
                "## Today's theme\n## Key expressions & vocabulary (with examples)\n"
                "## Practice exercises\n## Common mistakes & tips\n## Next steps"
            ),
            "lang_instruction": "Provide explanations in English. Write target language examples in the target language.",
        },
    },

    # ── Chat / チャット ────────────────────────────────────────────
    "chat": {
        "ja": {
            "role": (
                "あなたは以下に定義されたペルソナとして会話します。"
                "設定に忠実に、自然でリアルな会話を行ってください。"
            ),
            "fields": [
                ("persona", "ペルソナ（誰として話すか）", "例: 親しい友人 / 厳しい上司", False, [
                    "親しい友人（同世代）",
                    "厳しい上司・メンター",
                    "優しい先輩",
                    "ネイティブ英語話者の友人",
                    "医師・専門家",
                    "大学教授",
                    "起業家・投資家",
                    "面接官",
                    "カスタマーサポート担当",
                    "歴史上の人物",
                ]),
                ("personality", "性格・トーン", "例: フレンドリー・カジュアル", False, [
                    "フレンドリー・カジュアル",
                    "丁寧・フォーマル",
                    "厳しめ・直球",
                    "ユーモラス・陽気",
                    "論理的・分析的",
                    "共感的・サポーティブ",
                    "批判的・devil's advocate",
                    "ポジティブ・励ます",
                ]),
                ("expertise", "専門知識・背景", "例: IT業界10年", False, [
                    "IT・ソフトウェアエンジニアリング",
                    "AI・機械学習",
                    "ビジネス・経営",
                    "マーケティング・営業",
                    "医療・ヘルスケア",
                    "法律・コンプライアンス",
                    "ファイナンス・投資",
                    "教育・学術",
                    "デザイン・クリエイティブ",
                    "専門知識なし（一般人）",
                ]),
                ("language", "会話する言語", "例: 日本語 / 英語", False, [
                    "日本語", "英語", "スペイン語",
                    "英語（日本語でフィードバックあり）",
                    "日本語と英語を交互に",
                ]),
                ("purpose", "会話の目的", "例: 英会話練習・壁打ち", False, [
                    "雑談・気晴らし",
                    "英会話練習",
                    "面接練習",
                    "プレゼン練習",
                    "アイデアの壁打ち",
                    "ロールプレイ（ビジネスシミュレーション）",
                    "ロールプレイ（医療相談シミュレーション）",
                    "メンタルサポート・話し相手",
                    "ディベート練習",
                ]),
                ("question", "最初のシナリオ・依頼", "例: 私の自己紹介を聞いてフィードバックしてください", True, []),
                ("output_expectation", "期待する出力", "例: 自然な会話形式・返答後に改善点", False, [
                    "自然な会話形式のみ",
                    "返答後に改善点・フィードバックを添える",
                    "返答後に語彙・文法の補足をする",
                    "会話後にまとめ・評価を出す",
                ]),
            ],
            "rules": [
                "定義されたペルソナと性格に終始一貫して従ってください。",
                "自然でリアルな会話を心がけてください。",
                "会話練習の場合は、相手の発言の自然さや文法についてさりげなく補足してください。",
                "ロールプレイ中はペルソナを崩さないようにしてください。",
            ],
            "output_format": (
                "会話形式で返答してください。\n"
                "練習目的の場合は返答の最後に【フィードバック】セクションを追加し、"
                "改善点や良かった点を簡潔に伝えてください。"
            ),
            "lang_instruction": "会話する言語の設定に従ってください。設定がない場合は日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are roleplaying as the persona defined below. "
                "Stay true to the character and engage in natural, realistic conversation."
            ),
            "fields": [
                ("persona", "Persona (who you are)", "e.g. Close friend / Strict boss", False, [
                    "Close friend (same generation)",
                    "Strict boss / mentor",
                    "Supportive senior colleague",
                    "Native English speaker friend",
                    "Doctor / Specialist",
                    "University professor",
                    "Entrepreneur / Investor",
                    "Job interviewer",
                    "Customer support agent",
                    "Historical figure",
                ]),
                ("personality", "Personality & tone", "e.g. Friendly, casual", False, [
                    "Friendly & casual",
                    "Polite & formal",
                    "Direct & strict",
                    "Humorous & upbeat",
                    "Logical & analytical",
                    "Empathetic & supportive",
                    "Critical / Devil's advocate",
                    "Positive & encouraging",
                ]),
                ("expertise", "Expertise & background", "e.g. 10yr IT veteran", False, [
                    "IT / Software engineering",
                    "AI / Machine learning",
                    "Business / Management",
                    "Marketing / Sales",
                    "Medical / Healthcare",
                    "Legal / Compliance",
                    "Finance / Investment",
                    "Education / Academia",
                    "Design / Creative",
                    "No expertise (general person)",
                ]),
                ("language", "Conversation language", "e.g. English", False, [
                    "English", "Spanish", "Japanese",
                    "English (with Japanese feedback)",
                    "Alternating English and Japanese",
                ]),
                ("purpose", "Purpose", "e.g. English practice / Brainstorming", False, [
                    "Small talk / Casual chat",
                    "English conversation practice",
                    "Job interview practice",
                    "Presentation practice",
                    "Brainstorming / Rubber duck",
                    "Business simulation roleplay",
                    "Medical consultation simulation",
                    "Mental support / Companionship",
                    "Debate practice",
                ]),
                ("question", "Opening scenario / Request", "e.g. Listen to my intro and give feedback", True, []),
                ("output_expectation", "Expected output", "e.g. Natural dialogue + feedback after", False, [
                    "Natural dialogue only",
                    "Reply + improvement feedback",
                    "Reply + vocabulary/grammar notes",
                    "Conversation summary & evaluation",
                ]),
            ],
            "rules": [
                "Stay consistently in character throughout the entire conversation.",
                "Keep the conversation natural and realistic.",
                "For practice purposes, subtly point out unnatural expressions or grammar issues.",
                "Do not break character during roleplay.",
            ],
            "output_format": (
                "Respond in dialogue format.\n"
                "For practice purposes, add a [Feedback] section at the end of your reply "
                "with brief notes on what was good and what could be improved."
            ),
            "lang_instruction": "Follow the language setting defined above. Default to English if not specified.",
        },
    },

    # ── Recipe / レシピ ────────────────────────────────────────────
    "recipe": {
        "ja": {
            "role": (
                "あなたはプロの料理家兼栄養士です。"
                "ユーザーの食材・好み・状況に合わせて、実践的で美味しいレシピを提案します。"
                "家庭で再現しやすい手順と、プロのコツを織り交ぜた提案が得意です。"
            ),
            "fields": [
                ("request_type", "知りたいこと", "例: 材料からレシピ提案", False, [
                    "食材からレシピを提案してほしい",
                    "作りたい料理のレシピを教えてほしい",
                    "今ある食材で何が作れるか提案してほしい",
                    "ヘルシーなアレンジレシピを教えてほしい",
                    "簡単・時短レシピを教えてほしい",
                    "本格的なレシピを教えてほしい",
                    "余り物を使ったレシピを教えてほしい",
                    "特定の栄養素を意識したレシピを教えてほしい",
                ]),
                ("dish_category", "料理のカテゴリ", "例: 和食・パスタ・スープ", False, [
                    "和食（煮物・焼き物・炒め物）",
                    "洋食（パスタ・グラタン・ソテー）",
                    "中華（炒め物・蒸し料理）",
                    "アジア料理（タイ・韓国・インドなど）",
                    "スープ・鍋料理",
                    "サラダ・副菜",
                    "お弁当おかず",
                    "スイーツ・お菓子",
                    "パン・ピザ",
                    "おつまみ・前菜",
                    "朝食・ブランチ",
                    "丼・ご飯もの",
                ]),
                ("dish_name", "作りたい料理名", "例: カルボナーラ・肉じゃが（自由入力）", False, []),
                ("ingredients", "使いたい・使える材料", "例: 鶏もも肉・玉ねぎ・じゃがいも", False, []),
                ("servings", "何人分？", "例: 2人分", False, [
                    "1人分", "2人分", "3〜4人分", "4〜6人分（作り置き）",
                ]),
                ("preferences", "食の好み・好きなもの", "例: 濃いめの味付け・スパイシー好き", False, [
                    "あっさり・薄味", "濃いめ・しっかり味",
                    "甘辛", "スパイシー・辛め",
                    "さっぱり・柑橘系", "クリーミー・まろやか",
                    "和風だし風味", "洋風ハーブ系",
                ]),
                ("dislikes", "苦手なもの・嫌いなもの", "例: パクチー・レバー", False, [
                    "パクチー（香菜）", "レバー・内臓系",
                    "生魚・刺身", "辛いもの全般",
                    "苦い野菜（ゴーヤ・ピーマンなど）",
                    "なし（特になし）",
                ]),
                ("allergies", "アレルギー・食事制限", "例: 乳製品・グルテンフリー", False, [
                    "なし", "卵アレルギー", "乳製品アレルギー",
                    "小麦（グルテンフリー）", "甲殻類アレルギー",
                    "ナッツアレルギー", "大豆アレルギー",
                    "ベジタリアン", "ヴィーガン", "ハラール",
                ]),
                ("tools", "使えるキッチンツール", "例: 電子レンジのみ・フライパン・オーブン", False, [
                    "フライパン・鍋のみ",
                    "電子レンジのみ",
                    "オーブン・トースター使用可",
                    "炊飯器使用可",
                    "圧力鍋使用可",
                    "ミキサー・フードプロセッサー使用可",
                    "一般的な調理器具全て使用可",
                ]),
                ("time", "調理時間の目安", "例: 30分以内", False, [
                    "15分以内（超時短）",
                    "30分以内",
                    "1時間以内",
                    "時間をかけてOK（2時間以上も可）",
                    "前日仕込みOK",
                ]),
                ("output_expectation", "期待する出力", "例: レシピ1つ・詳しい手順付き", False, [
                    "レシピ1つ（材料・手順・コツ付き）",
                    "レシピ3つ提案（簡単な説明付き）",
                    "材料からアイデアを3つ提案",
                    "詳しい手順＋プロのコツ付き",
                    "カロリー・栄養情報付き",
                    "アレンジバリエーション付き",
                    "作り置き・保存方法付き",
                ]),
            ],
            "rules": [
                "材料の分量は人数分に合わせて具体的な数値で記載してください。",
                "手順は番号付きで、1ステップずつ明確に書いてください。",
                "調理のコツや失敗しやすいポイントを必ず1つ以上含めてください。",
                "アレルギーや食事制限が指定されている場合は必ず厳守してください。",
                "嫌いな食材は代替案も提示してください。",
            ],
            "output_format": (
                "以下の形式で出力してください：\n"
                "## 料理名\n"
                "### 材料（〇人分）\n"
                "### 手順\n"
                "### コツ・ポイント\n"
                "### カロリー概算\n"
                "### アレンジ提案（任意）"
            ),
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a professional chef and nutritionist. "
                "You suggest practical and delicious recipes tailored to the user's ingredients, preferences, and situation. "
                "You excel at combining easy-to-follow home cooking steps with professional tips."
            ),
            "fields": [
                ("request_type", "What you want to know", "e.g. Suggest recipes from ingredients", False, [
                    "Suggest recipes from my ingredients",
                    "Give me the recipe for a specific dish",
                    "What can I make with what I have?",
                    "Suggest a healthy version of a dish",
                    "Quick & easy recipes only",
                    "Authentic / elaborate recipe",
                    "Use up leftovers",
                    "Recipes focused on specific nutrition",
                ]),
                ("dish_category", "Dish category", "e.g. Pasta, Soup, Stir-fry", False, [
                    "Japanese cuisine",
                    "Western / European",
                    "Italian (pasta, pizza)",
                    "Chinese (stir-fry, steamed)",
                    "Asian (Thai, Korean, Indian)",
                    "Soups & stews",
                    "Salads & sides",
                    "Lunchbox / meal prep",
                    "Desserts & baking",
                    "Breakfast & brunch",
                    "Rice bowls & grains",
                    "Snacks & appetizers",
                ]),
                ("dish_name", "Dish name (if specific)", "e.g. Carbonara, Beef stew (free input)", False, []),
                ("ingredients", "Ingredients to use", "e.g. chicken thigh, onion, potato", False, []),
                ("servings", "Servings", "e.g. 2 servings", False, [
                    "1 serving", "2 servings", "3-4 servings", "4-6 servings (meal prep)",
                ]),
                ("preferences", "Food preferences / likes", "e.g. Rich flavor, spicy", False, [
                    "Light & mild", "Rich & savory",
                    "Sweet & savory", "Spicy",
                    "Refreshing / citrusy", "Creamy & mellow",
                    "Umami-forward", "Herby & aromatic",
                ]),
                ("dislikes", "Dislikes / foods to avoid", "e.g. Cilantro, liver", False, [
                    "Cilantro (coriander)", "Liver / organ meats",
                    "Raw fish", "Spicy food",
                    "Bitter vegetables", "None",
                ]),
                ("allergies", "Allergies / dietary restrictions", "e.g. Dairy-free, gluten-free", False, [
                    "None", "Egg allergy", "Dairy-free",
                    "Gluten-free", "Shellfish allergy",
                    "Nut allergy", "Soy allergy",
                    "Vegetarian", "Vegan", "Halal",
                ]),
                ("tools", "Available kitchen tools", "e.g. Microwave only, frying pan, oven", False, [
                    "Frying pan & pot only",
                    "Microwave only",
                    "Oven / toaster oven available",
                    "Rice cooker available",
                    "Pressure cooker available",
                    "Blender / food processor available",
                    "Full kitchen equipment",
                ]),
                ("time", "Cooking time available", "e.g. Under 30 minutes", False, [
                    "Under 15 minutes (super quick)",
                    "Under 30 minutes",
                    "Under 1 hour",
                    "Happy to spend 2+ hours",
                    "Overnight / advance prep OK",
                ]),
                ("output_expectation", "Expected output", "e.g. 1 recipe with detailed steps", False, [
                    "1 recipe (ingredients, steps, tips)",
                    "3 recipe suggestions (brief overview)",
                    "3 ideas from my ingredients",
                    "Detailed steps + professional tips",
                    "With calorie & nutrition info",
                    "With variation ideas",
                    "With storage & meal prep tips",
                ]),
            ],
            "rules": [
                "Provide specific quantities for ingredients based on the number of servings.",
                "Write steps in numbered format, one clear action per step.",
                "Always include at least one cooking tip or common mistake to avoid.",
                "Strictly follow any allergy or dietary restrictions.",
                "Suggest substitutes for any disliked ingredients.",
            ],
            "output_format": (
                "Output in this format:\n"
                "## Dish name\n"
                "### Ingredients (serves X)\n"
                "### Instructions\n"
                "### Tips & tricks\n"
                "### Estimated calories\n"
                "### Variations (optional)"
            ),
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Other / その他 ─────────────────────────────────────────────
    "other": {
        "ja": {
            "role": (
                "あなたは幅広い知識を持つ優秀なアシスタントです。"
                "ユーザーの目的に応じて最適な回答を提供します。"
            ),
            "fields": [
                ("goal", "目的・ゴール", "例: このタスクで達成したいこと", False, [
                    "情報収集・調査", "文章の作成・編集", "アイデア出し・ブレスト",
                    "問題解決・トラブルシューティング", "意思決定のサポート",
                    "要約・整理", "翻訳", "データ分析", "プレゼン資料作成",
                ]),
                ("background", "背景・文脈", "例: 現在の状況や前提条件", False, []),
                ("constraint", "制約・条件", "例: 文字数・形式・ツール", False, [
                    "200文字以内", "400文字以内", "800文字以内",
                    "箇条書きで", "表形式で", "です・ます調で",
                    "だ・である調で", "専門用語を使わずに",
                ]),
                ("question", "質問・依頼内容", "例: 具体的に何をしてほしいか", True, []),
                ("output_expectation", "期待する出力", "例: 箇条書き3点・表形式", False, [
                    "箇条書き（3〜5点）", "表形式", "コードブロック",
                    "文章（です・ます調）", "文章（だ・である調）",
                    "メール形式", "レポート形式", "FAQ形式",
                    "ステップバイステップ",
                ]),
            ],
            "rules": [],
            "output_format": (
                "ユーザーの指定した形式に従って出力してください。"
                "形式の指定がない場合は最も読みやすい形式を選んでください。"
            ),
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a highly capable assistant with broad knowledge. "
                "You provide optimal responses tailored to the user's needs."
            ),
            "fields": [
                ("goal", "Goal", "e.g. What you want to achieve", False, [
                    "Research & information gathering", "Writing & editing",
                    "Brainstorming / Ideation", "Problem solving",
                    "Decision support", "Summarization", "Translation",
                    "Data analysis", "Presentation creation",
                ]),
                ("background", "Background", "e.g. Current situation and context", False, []),
                ("constraint", "Constraints", "e.g. Length, format, tools", False, [
                    "Under 100 words", "Under 300 words",
                    "Bullet points", "Table format",
                    "Formal tone", "Casual tone",
                    "No technical jargon",
                ]),
                ("question", "Question / Request", "e.g. What specifically you need", True, []),
                ("output_expectation", "Expected output", "e.g. 3 bullet points, table format", False, [
                    "Bullet points (3-5)", "Table format", "Code block",
                    "Formal prose", "Casual prose", "Email format",
                    "Report format", "FAQ format", "Step-by-step",
                ]),
            ],
            "rules": [],
            "output_format": (
                "Follow the user's specified format. "
                "If no format is specified, choose the most readable one."
            ),
            "lang_instruction": "Please respond in English.",
        },
    },
}


# ────────────────────────────────────────────
# プロンプト組み立て関数
# ────────────────────────────────────────────
def build_prompt(
    category_key: str,
    lang: str,
    user_inputs: dict,
    profile: dict = None,
    simple_mode: bool = False,
    context_history: str = "",
    instructions: str = "",
    include_profile: bool = True,
    role_perspectives: str = "",
) -> str:
    tmpl = TEMPLATES[category_key][lang]

    if simple_mode:
        parts = []
        if instructions and instructions.strip():
            label = "【指示・ルール】" if lang == "ja" else "【Instructions】"
            inst_lines = [f"- {l.strip()}" for l in instructions.strip().splitlines() if l.strip()]
            parts.append(f"{label}\n" + "\n".join(inst_lines) + "\n")
        if context_history and context_history.strip():
            label = "【これまでの会話履歴】" if lang == "ja" else "【Conversation History】"
            parts.append(f"{label}\n{context_history.strip()}\n")
        label_q = "【追加の質問】" if lang == "ja" else "【Follow-up Question】"
        parts.append(f"{label_q}\n{user_inputs.get('question', '').strip()}")
        return "\n".join(parts)

    parts = []

    # 1. AIへの指示・ルール（最初に置くことでAIが確実に認識）
    if instructions and instructions.strip():
        label = "【指示・ルール】" if lang == "ja" else "【Instructions】"
        inst_lines = [f"- {l.strip()}" for l in instructions.strip().splitlines() if l.strip()]
        parts.append(f"{label}\n" + "\n".join(inst_lines) + "\n")

    # 2. ユーザー情報（include_profile が True の場合のみ）
    if include_profile and profile:
        profile_lines = []
        for key, val in profile.items():
            if key.startswith("_"):
                continue
            if val and str(val).strip():
                profile_lines.append(f"- {key}: {str(val).strip()}")
        if profile_lines:
            label = "【ユーザー情報】" if lang == "ja" else "【User Profile】"
            parts.append(label)
            parts.extend(profile_lines)
            parts.append("")

    # 3. 役割定義（スキル・経験・スタンスの3点セット）
    if lang == "ja":
        role_base = (
            "【役割】\n"
            "以下の3点を踏まえた専門家・アシスタントとして回答してください。\n"
            "- スキル: この質問・依頼に最も関連する専門領域・得意分野を自ら設定する\n"
            "- 経験: 実務・研究・現場での豊富な経験を持つ専門家として\n"
            "- スタンス: 正確さと実用性を重視し、不確かな情報は必ず明示する\n"
        )
        if role_perspectives and role_perspectives.strip():
            role_base += f"- 視点: {role_perspectives.strip()} の立場から回答する\n"
    else:
        role_base = (
            "【Role】\n"
            "Respond as an expert/assistant based on the following 3 points:\n"
            "- Skills: Set the most relevant expertise and specialty for this request\n"
            "- Experience: As a practitioner with substantial real-world experience\n"
            "- Stance: Prioritize accuracy and practicality; always flag uncertain information\n"
        )
        if role_perspectives and role_perspectives.strip():
            role_base += f"- Perspective: Respond from the viewpoint of {role_perspectives.strip()}\n"
    parts.append(role_base)

    # 4. 会話履歴・背景コンテキスト（あれば）
    if context_history and context_history.strip():
        if lang == "ja":
            parts.append(
                "【これまでの会話履歴・背景コンテキスト】\n"
                "以下は別のAIとの会話履歴または背景情報です。"
                "この内容を十分に理解した上で、以下の質問・依頼に回答してください。\n"
                f"{context_history.strip()}\n"
            )
        else:
            parts.append(
                "【Conversation History / Background Context】\n"
                "The following is a conversation history from another AI or background information. "
                "Please fully understand this context before answering the question below.\n"
                f"{context_history.strip()}\n"
            )

    # 5. 質問・依頼内容（値があるフィールドのみ）
    input_lines = []
    for field in tmpl["fields"]:
        field_key = field[0]
        label = field[1]
        value = user_inputs.get(field_key, "").strip()
        if value:
            if isinstance(label, dict):
                clean_label = label.get(lang) or label.get("ja") or field_key
            else:
                clean_label = label.replace(" *", "")
            input_lines.append(f"- {clean_label}: {value}")
    if input_lines:
        parts.append("【質問・依頼内容】" if lang == "ja" else "【Request】")
        parts.extend(input_lines)

    # 6. 出力ルール（カテゴリルール＋出力形式＋言語指示を統合、全て箇条書き）
    out_label = "【出力ルール】" if lang == "ja" else "【Output Rules】"
    out_lines = [f"- {rule}" for rule in tmpl["rules"]]
    # output_format が複数行の場合は各行に - を付ける
    for line in tmpl["output_format"].splitlines():
        line = line.strip()
        if line:
            out_lines.append(f"- {line}" if not line.startswith("-") else line)
    out_lines.append(f"- {tmpl['lang_instruction']}")
    parts.append(f"\n{out_label}\n" + "\n".join(out_lines))

    return "\n".join(parts)