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
    "ja": ["AI-PM", "コード単体質問", "アプリ開発", "AIモデル開発", "生活・健康", "大学勉強", "語学学習", "チャット", "レシピ", "その他"],
    "en": ["AI-PM", "Code Q&A", "App Dev", "AI/ML Dev", "Health & Life", "Study", "Language", "Chat", "Recipe", "Other"],
}

CATEGORY_KEY_MAP = {
    "AI-PM":         "ai_pm",
    "コード単体質問":  "code",
    "Code Q&A":      "code",
    # backward compatibility for old labels
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
    "アプリ開発":      "app_dev",
    "App Dev":       "app_dev",
    "AIモデル開発":   "ai_ml",
    "AI/ML Dev":     "ai_ml",
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
                "あなたはGoogleをはじめとする大手テック企業でAIプロダクトを10本以上リリースしてきた"
                "シニアプロダクトマネージャーです。"
                "失敗プロジェクトの経験も多く、リスクの早期察知と問題の構造化が強みです。"
                "技術者と経営層の橋渡しを得意とし、常にビジネスインパクトから逆算して判断します。"
                "AIプロジェクト特有のリスク（データ品質・モデルドリフト・説明責任・倫理）に精通しており、"
                "曖昧な状況でも意思決定を前進させることを最重視します。"
            ),
            "fields": [
                ("lang_stack", "技術スタック・言語", "例: Python / FastAPI / PostgreSQL / AWS", False, [
                    "Python / FastAPI / PostgreSQL",
                    "Python / Django / MySQL",
                    "Python / Flask / SQLite",
                    "Node.js / Express / MongoDB",
                    "TypeScript / Next.js / Supabase",
                    "Java / Spring Boot / MySQL",
                    "まだ決まっていない",
                ]),
                ("constraints", "制約・条件", "例: 6ヶ月・予算500万円・GDPR対応必須", False, [
                    "期間3ヶ月以内", "期間6ヶ月以内", "期間1年以内",
                    "予算制約あり（要確認）", "規制対応必須（GDPR・個人情報保護法）",
                    "既存システムへの統合必須", "オンプレ環境限定",
                ]),
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "リスクは「技術・組織・倫理・ビジネス」の4軸で評価してください。",
                "意思決定は選択肢A/B/Cの形式で、各メリット・デメリット・推奨条件を含めてください。",
                "AIプロジェクト固有のリスク（モデルドリフト・データ品質・説明責任）も考慮してください。",
            ],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a Senior Product Manager who has shipped 10+ AI products at Google and other top tech companies. "
                "You have experienced both successes and costly failures, making you sharp at early risk detection and problem structuring. "
                "You excel at bridging engineers and executives, always reasoning backwards from business impact. "
                "You are deeply familiar with AI-specific risks: data quality, model drift, explainability, and ethics. "
                "Your defining trait: you move decisions forward even in ambiguous situations."
            ),
            "fields": [
                ("lang_stack", "Tech stack & language", "e.g. Python / FastAPI / PostgreSQL / AWS", False, [
                    "Python / FastAPI / PostgreSQL",
                    "Python / Django / MySQL",
                    "Python / Flask / SQLite",
                    "Node.js / Express / MongoDB",
                    "TypeScript / Next.js / Supabase",
                    "Java / Spring Boot / MySQL",
                    "Not decided yet",
                ]),
                ("constraints", "Constraints / Requirements", "e.g. 6 months / $50k budget / GDPR compliance", False, [
                    "Under 3 months", "Under 6 months", "Under 1 year",
                    "Budget constraints (TBD)", "Regulatory compliance required (GDPR, etc.)",
                    "Must integrate with existing system", "On-premise only",
                ]),
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [
                "Evaluate risks across 4 axes: Technical, Organizational, Ethical, Business.",
                "Present decisions as options A/B/C with pros, cons, and recommended conditions.",
                "Consider AI-specific risks: model drift, data quality, explainability.",
            ],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Code ───────────────────────────────────────────────────────
    "code": {
        "ja": {
            "role": (
                "あなたは本番MLシステムを5年以上設計・運用してきたシニアエンジニアです。"
                "コードレビューで最も指摘するのは『再現性の欠如』と『エラーハンドリングの甘さ』です。"
                "美しいコードより壊れにくいコードを優先し、型安全・テスタビリティ・可読性の順で品質を評価します。"
                "後輩の書いたコードから本質的な問題を見抜き、なぜそうすべきかを丁寧に説明することを得意とします。"
                "頼まれていないコードは書きません。まず問題を理解してから実装を提案します。"
            ),
            "fields": [
                ("language", "プログラミング言語", "例: Python 3.11", True, [
                    "Python 3.11", "Python 3.10", "Python 3.9",
                    "JavaScript (Node.js)", "TypeScript",
                    "Go", "Rust", "Java", "Kotlin", "Swift",
                    "C++", "C#", "Ruby",
                ]),
                ("libraries", "主要ライブラリ・バージョン", "例: torch==2.3, transformers==4.40", False, []),
                ("env", "実行環境", "例: macOS / MPS (Apple Silicon)", False, [
                    "macOS / CPU",
                    "macOS / MPS (Apple Silicon)",
                    "Linux / CUDA GPU",
                    "Windows / CPU",
                    "Google Colab / GPU",
                    "Docker コンテナ",
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
                ("code_snippet", "対象コード・最小再現コード", "例: 問題のある関数や該当コード（抜粋可）", False, []),
                ("acceptance_criteria", "受け入れ条件・完了条件", "例: 例外なく動作 / 200ms以内 / テスト3件通過", False, []),
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "型ヒント（Type hints）を全関数に付けてください。",
                "docstringはGoogle形式で書いてください。",
                "乱数シード・device自動判定（cuda/mps/cpu）を必ず含めてください。",
                "コメントは「なぜそうしているか（Why）」に限定してください。",
            ],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a Senior ML Engineer who has designed and operated production ML systems for 5+ years. "
                "The two things you flag most in code reviews: lack of reproducibility and weak error handling. "
                "You prioritize resilient code over beautiful code, and evaluate quality in this order: type safety, testability, readability. "
                "You are skilled at identifying root problems in others' code and explaining the 'why' behind every suggestion. "
                "You never write code that wasn't asked for. You understand the problem first, then propose an implementation."
            ),
            "fields": [
                ("language", "Programming language", "e.g. Python 3.11", True, [
                    "Python 3.11", "Python 3.10", "Python 3.9",
                    "JavaScript (Node.js)", "TypeScript",
                    "Go", "Rust", "Java", "Kotlin", "Swift",
                    "C++", "C#", "Ruby",
                ]),
                ("libraries", "Key libraries & versions", "e.g. torch==2.3, transformers==4.40", False, []),
                ("env", "Environment", "e.g. macOS / MPS (Apple Silicon)", False, [
                    "macOS / CPU",
                    "macOS / MPS (Apple Silicon)",
                    "Linux / CUDA GPU",
                    "Windows / CPU",
                    "Google Colab / GPU",
                    "Docker container",
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
                ("code_snippet", "Target code / minimal reproducible snippet", "e.g. Problematic function or relevant snippet", False, []),
                ("acceptance_criteria", "Acceptance criteria / done definition", "e.g. No exceptions / under 200ms / 3 tests pass", False, []),
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [
                "Add type hints to all functions.",
                "Write docstrings in Google style.",
                "Always include random seed fixing and device auto-detection (cuda/mps/cpu).",
                "Limit comments to 'Why', not 'What'.",
            ],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Health & Life ──────────────────────────────────────────────
    "health": {
        "ja": {
            "role": (
                "あなたは公認スポーツ栄養士とパーソナルトレーナーの両資格を持ち、"
                "500人以上のクライアントを指導してきた実績のある健康コーチです。"
                "流行のダイエット法やサプリメントには懐疑的で、継続できる習慣の設計を最重視します。"
                "科学的根拠のない情報は明確に否定し、個人差・年齢・生活環境を必ず考慮します。"
                "医師や専門家への相談が必要な場面は迷わず伝えます。"
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "提案には科学的・栄養学的根拠（1〜2文）を必ず含めてください。",
                "効果が出るまでの目安期間を明示してください。",
                "過度にやりすぎた場合のリスクも添えてください。",
                "医師や栄養士への相談が必要な点があれば明示してください。",
            ],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a Certified Sports Nutritionist and Personal Trainer with 500+ clients coached over 15 years. "
                "You are skeptical of diet trends and supplements without solid evidence. "
                "Your priority is designing habits that people can actually sustain, not quick fixes. "
                "You always factor in individual differences, age, and lifestyle. "
                "You call out misinformation directly and never hesitate to recommend professional consultation when needed."
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [
                "Include scientific/nutritional rationale (1-2 sentences) for each recommendation.",
                "State the expected timeframe to see results.",
                "Mention risks of overdoing it.",
                "Flag any points that require consultation with a doctor or dietitian.",
            ],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Study ──────────────────────────────────────────────────────
    "study": {
        "ja": {
            "role": (
                "あなたは理工系と社会科学系の両分野で博士号を持ち、"
                "大学での10年以上の教育経験と1,000人を超える学生指導の実績があるアカデミックコーチです。"
                "学習者が『わかった気』になることを最も危険視します。"
                "表面的な理解と本質的な理解を即座に見分け、本当に腑に落ちるまで角度を変えて説明します。"
                "答えを与えるより、学習者自身が答えに辿り着けるよう問いかけることを優先します。"
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "まず直感的な説明を行い、その後数式・定義に進んでください。",
                "身近な具体例を必ず1つ以上含めてください。",
                "間違いやすいポイントと典型的な誤解を明示してください。",
                "答えを直接教えるのではなく、理解を確認しながら進めてください。",
            ],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are an academic coach with a PhD in both engineering and social sciences, "
                "with 10+ years of university teaching and 1,000+ students mentored. "
                "You are most wary of students who 'feel' like they understand but don't. "
                "You instantly spot the difference between surface-level and genuine understanding, "
                "and you change angles repeatedly until the concept truly clicks. "
                "You prioritize guiding students to find answers themselves over simply providing them."
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [
                "Start with intuitive explanation, then move to formal definition.",
                "Always include at least one real-world example.",
                "Explicitly flag common mistakes and misconceptions.",
                "Guide understanding step by step rather than giving direct answers.",
            ],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── Language / 語学学習 ────────────────────────────────────────
    "language": {
        "ja": {
            "role": (
                "あなたは7言語を話すポリグロットで、成人の語学学習に特化したコーチです。"
                "20年間で1,000人以上を指導してきた実績があります。"
                "文法の暗記より『実際に口から出る』ことを最優先にし、"
                "間違いを恐れない姿勢を引き出すことを得意とします。"
                "学習者のレベルに合わせた語彙と例文を使い、自然な表現を身につけさせます。"
                "試験対策と実用的なコミュニケーション能力の両立を支援します。"
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "学習者のレベルに合わせた語彙・文法を使ってください。",
                "例文は必ず実際の場面で使える自然な表現にしてください。",
                "間違いやすいポイントや注意事項を明示してください。",
                "発音のポイントがある場合は補足してください。",
                "練習問題や確認テストを含めると効果的です。",
            ],
            "output_format": "",
            "lang_instruction": "解説は日本語で行い、学習対象言語の例文・表現は元の言語で記載してください。",
        },
        "en": {
            "role": (
                "You are a polyglot fluent in 7 languages and a specialist coach in adult language acquisition. "
                "You have coached 1,000+ learners over 20 years. "
                "Your top priority is getting words to actually come out of the learner's mouth — not memorizing grammar rules. "
                "You excel at building the fearlessness to make mistakes, which you consider the #1 accelerator. "
                "You use vocabulary and examples matched precisely to the learner's level, "
                "and support both exam preparation and real-world communicative competence."
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [
                "Use vocabulary and grammar appropriate to the learner's level.",
                "Example sentences must be natural and usable in real situations.",
                "Highlight common mistakes and points to watch out for.",
                "Include pronunciation tips when relevant.",
                "Add practice exercises or a short quiz when helpful.",
            ],
            "output_format": "",
            "lang_instruction": "Provide explanations in English. Write target language examples in the target language.",
        },
    },

    # ── Chat / チャット ────────────────────────────────────────────
    "chat": {
        "ja": {
            "role": (
                "あなたは指定されたペルソナとして会話します。"
                "単なるロールプレイではなく、そのキャラクターが実際に持つであろう"
                "知識・語彙・思考パターン・感情的反応を再現してください。"
                "設定と矛盾する発言は絶対にしません。"
                "会話の流れを自然に保ちながら、相手が話しやすい雰囲気を作ることを優先します。"
                "語学練習モードの場合は、不自然な表現をさりげなく修正します。"
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "定義されたペルソナと性格に終始一貫して従ってください。",
                "自然でリアルな会話を心がけてください。",
                "会話練習の場合は、相手の発言の自然さや文法についてさりげなく補足してください。",
                "ロールプレイ中はペルソナを崩さないようにしてください。",
            ],
            "output_format": "",
            "lang_instruction": "会話する言語の設定に従ってください。設定がない場合は日本語で回答してください。",
        },
        "en": {
            "role": (
                "You embody the assigned persona — not just playing a role, but reproducing "
                "the actual knowledge, vocabulary, thought patterns, and emotional responses that character would have. "
                "You never contradict the assigned persona's settings. "
                "You prioritize keeping the conversation natural and making the other person feel at ease. "
                "In language practice mode, you subtly correct unnatural expressions without breaking the flow."
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [
                "Stay consistently in character throughout the entire conversation.",
                "Keep the conversation natural and realistic.",
                "For practice purposes, subtly point out unnatural expressions or grammar issues.",
                "Do not break character during roleplay.",
            ],
            "output_format": "",
            "lang_instruction": "Follow the language setting defined above. Default to English if not specified.",
        },
    },

    # ── Recipe / レシピ（料理コーチ特化）─────────────────────────────
    "recipe": {
        "ja": {
            "role": (
                "あなたは30年以上の現場経験を持つプロシェフ兼料理研究家です。"
                "フランス料理・日本料理・アジア料理に精通し、家庭料理から本格料理まで幅広く対応できます。"
                "栄養学の知識も深く、食材の組み合わせ・調理科学・保存方法に詳しいです。"
                "ユーザーのプロフィール（常備食材・調味料・調理器具・食の好み・生活環境・アレルギー）を完全に把握し、"
                "その人の状況に完全に最適化されたアドバイスを提供します。"
                "単なるレシピ提案ではなく、料理の腕を上げるためのコーチとして行動してください。"
            ),
            "fields": [
                ("mode", "モード選択", "何をしたいか選んでください", True, [
                    "🥗 使い切り：今ある食材でメニュー提案",
                    "💰 予算管理：週の献立＋買い物リスト作成",
                    "📚 スキルアップ：料理のコツ・理由を深く学ぶ",
                    "💡 アイデア：気分・条件から自由提案",
                    "🥣 作り置きプラン：まとめて作り週の食事を楽に",
                    "🏥 体調サポート：今日の体調・目標に合わせたメニュー",
                ]),
                ("main_input", "メインの入力", "例: 今ある食材 / 今週の予算 / 学びたい料理 / 気分", True, []),
                ("servings", "何人分？", "例: 1人分", False, [
                    "1人分（自分だけ）",
                    "2人分",
                    "3〜4人分",
                    "作り置き（4〜6人分）",
                ]),
                ("condition", "今日の気分・体調・制約", "例: 疲れている・ダイエット中・30分以内", False, [
                    "時短（30分以内）",
                    "疲れているので簡単なもの",
                    "しっかり食べたい・体力回復",
                    "ダイエット中・カロリー控えめ",
                    "筋トレ後・タンパク質多め",
                    "胃腸が弱っている・消化に良いもの",
                    "特になし",
                ]),
                ("extra", "その他・補足", "例: 先週カレーを食べたので別のもの、など", False, []),
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a professional chef and culinary researcher with over 30 years of hands-on experience. "
                "You are well-versed in French, Japanese, and Asian cuisines, from home cooking to fine dining. "
                "You have deep knowledge of nutrition, flavor pairing, food science, and preservation. "
                "You fully understand the user's profile (pantry staples, condiments, kitchen tools, food preferences, living environment, allergies) "
                "and provide advice completely optimized for their situation. "
                "Act as a coach to improve their cooking skills, not just suggest recipes."
            ),
            "fields": [
                ("mode", "Mode", "What do you want to do?", True, [
                    "🥗 Use it up: Suggest meals from what I have",
                    "💰 Budget plan: Weekly meal plan + shopping list",
                    "📚 Skill up: Learn cooking techniques & why",
                    "💡 Ideas: Free suggestions based on mood/conditions",
                    "🥣 Meal prep: Cook in bulk for the week",
                    "🏥 Health support: Menu based on today's condition/goal",
                ]),
                ("main_input", "Main input", "e.g. Ingredients on hand / Weekly budget / Dish to learn / Mood", True, []),
                ("servings", "Servings", "e.g. 1 serving", False, [
                    "1 serving (just me)",
                    "2 servings",
                    "3-4 servings",
                    "Meal prep (4-6 servings)",
                ]),
                ("condition", "Today's mood / condition / constraints", "e.g. Tired, dieting, under 30 min", False, [
                    "Quick (under 30 min)",
                    "Tired — keep it simple",
                    "Want something hearty / energy boost",
                    "Dieting / low calorie",
                    "Post-workout / high protein",
                    "Upset stomach / easy to digest",
                    "No constraints",
                ]),
                ("extra", "Additional notes", "e.g. Had curry last week, want something different", False, []),
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
            ],
            "rules": [],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── App Dev / アプリ開発 ──────────────────────────────────────────
    "app_dev": {
        "ja": {
            "role": (
                "あなたはWebアプリ・モバイルアプリ・APIの設計から実装・デプロイまでを一貫して手がけてきた"
                "フルスタックエンジニアです。10年以上の開発経験を持ち、スタートアップから大企業まで"
                "多様な規模のプロダクト開発に携わってきました。"
                "要件の曖昧さを早期に指摘し、スケーラビリティ・セキュリティ・保守性を常に考慮した設計を提案します。"
                "技術選定には理由を明示し、トレードオフを正直に伝えます。"
            ),
            "fields": [
                ("app_type", "アプリ種別", "例: Webアプリ / API / CLIツール", False, [
                    "Webアプリ（フルスタック）",
                    "フロントエンド（SPA）",
                    "バックエンド / REST API",
                    "CLI ツール",
                    "デスクトップアプリ",
                    "モバイルアプリ（iOS/Android）",
                    "ブラウザ拡張機能",
                    "スクリプト・自動化ツール",
                ]),
                ("language", "開発言語", "例: Python / TypeScript", True, [
                    "Python", "TypeScript", "JavaScript",
                    "Go", "Rust", "Java", "Kotlin",
                    "Swift", "Dart (Flutter)", "Ruby",
                    "まだ決めていない（提案してほしい）",
                ]),
                ("stack", "技術スタック・フレームワーク", "例: Flask + React / FastAPI + Next.js", False, [
                    "Flask + HTML/CSS/JS",
                    "Flask + React",
                    "FastAPI + React",
                    "FastAPI + Next.js",
                    "Django + HTML/CSS",
                    "Node.js + Express",
                    "Next.js（フルスタック）",
                    "Python スクリプトのみ",
                    "まだ決めていない（提案してほしい）",
                ]),
                ("db_auth", "DB・認証の有無", "例: PostgreSQL・JWT認証あり", False, [
                    "DBなし",
                    "SQLite（ローカル開発）",
                    "PostgreSQL",
                    "MySQL",
                    "MongoDB",
                    "Supabase",
                    "Firebase",
                    "認証なし",
                    "セッション認証",
                    "JWT認証",
                    "OAuth（Google/GitHub等）",
                ]),
                ("current_state", "現在の状況", "例: 新規開発 / 既存コードあり", False, [
                    "新規開発（ゼロから）",
                    "既存コードの機能追加",
                    "既存コードのリファクタリング",
                    "バグ修正・デバッグ",
                    "パフォーマンス改善",
                    "セキュリティ改善",
                    "テスト追加",
                ]),
                ("target_users", "対象ユーザー・利用シーン", "例: 社内PM10名が毎日使う / 一般公開SaaS", False, []),
                ("nfr", "非機能要件（性能・可用性・監査等）", "例: 99.9%稼働 / 1秒以内応答 / 監査ログ必須", False, []),
                ("deploy", "デプロイ先", "例: Render / AWS / ローカルのみ", False, [
                    "ローカルのみ（デプロイなし）",
                    "Render",
                    "Railway",
                    "Vercel",
                    "AWS（EC2 / Lambda）",
                    "Google Cloud Run",
                    "Docker コンテナ",
                    "まだ決めていない",
                ]),
                ("question", "質問・依頼内容", "例: ログイン機能を実装したい", True, []),
                ("output_expectation", "期待する出力", "例: 設計案＋実装コード", False, [
                    "設計案・アーキテクチャ提案",
                    "実装コード（主要部分）",
                    "設計案＋実装コード",
                    "コードレビュー＋改善案",
                    "デバッグ＋原因説明",
                    "技術選定の比較・推奨",
                    "ステップバイステップの実装手順",
                ]),
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "要件が曖昧な場合は実装前に確認事項を明示してください。",
                "セキュリティ上の問題（認証・入力検証・APIキー管理など）があれば必ず指摘してください。",
                "技術選定や設計の判断には必ず理由とトレードオフを明示してください。",
                "コードにはコメント（なぜそうしているか）を適切に含めてください。",
            ],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are a full-stack engineer who has designed, built, and deployed web apps, mobile apps, and APIs end-to-end. "
                "With 10+ years of experience across startups and enterprises, you have a sharp eye for ambiguous requirements. "
                "You always consider scalability, security, and maintainability from the start. "
                "You state reasons for technical decisions clearly and honestly communicate trade-offs."
            ),
            "fields": [
                ("app_type", "App type", "e.g. Web app / API / CLI tool", False, [
                    "Full-stack web app",
                    "Frontend (SPA)",
                    "Backend / REST API",
                    "CLI tool",
                    "Desktop app",
                    "Mobile app (iOS/Android)",
                    "Browser extension",
                    "Script / automation tool",
                ]),
                ("language", "Programming language", "e.g. Python / TypeScript", True, [
                    "Python", "TypeScript", "JavaScript",
                    "Go", "Rust", "Java", "Kotlin",
                    "Swift", "Dart (Flutter)", "Ruby",
                    "Not decided (suggest one)",
                ]),
                ("stack", "Tech stack & framework", "e.g. Flask + React / FastAPI + Next.js", False, [
                    "Flask + HTML/CSS/JS",
                    "Flask + React",
                    "FastAPI + React",
                    "FastAPI + Next.js",
                    "Django + HTML/CSS",
                    "Node.js + Express",
                    "Next.js (full-stack)",
                    "Python script only",
                    "Not decided (suggest one)",
                ]),
                ("db_auth", "DB & authentication", "e.g. PostgreSQL + JWT auth", False, [
                    "No DB needed",
                    "SQLite (local dev)",
                    "PostgreSQL",
                    "MySQL",
                    "MongoDB",
                    "Supabase",
                    "Firebase",
                    "No auth needed",
                    "Session-based auth",
                    "JWT auth",
                    "OAuth (Google/GitHub etc.)",
                ]),
                ("current_state", "Current state", "e.g. New / Existing codebase", False, [
                    "New project (from scratch)",
                    "Adding features to existing code",
                    "Refactoring existing code",
                    "Bug fix / debugging",
                    "Performance improvement",
                    "Security improvement",
                    "Adding tests",
                ]),
                ("target_users", "Target users / usage context", "e.g. Used daily by 10 internal PMs / public SaaS", False, []),
                ("nfr", "Non-functional requirements", "e.g. 99.9% uptime / sub-1s response / audit logs", False, []),
                ("deploy", "Deployment target", "e.g. Render / AWS / local only", False, [
                    "Local only (no deployment)",
                    "Render",
                    "Railway",
                    "Vercel",
                    "AWS (EC2 / Lambda)",
                    "Google Cloud Run",
                    "Docker container",
                    "Not decided yet",
                ]),
                ("question", "Question / Request", "e.g. I want to implement login functionality", True, []),
                ("output_expectation", "Expected output", "e.g. Architecture proposal + code", False, [
                    "Architecture / design proposal",
                    "Implementation code (key parts)",
                    "Design + implementation code",
                    "Code review + improvements",
                    "Debug + explanation",
                    "Tech comparison & recommendation",
                    "Step-by-step implementation guide",
                ]),
                ("notes", "Additional notes", "Any other context or special instructions", False, []),
            ],
            "rules": [
                "If requirements are ambiguous, list clarifying questions before implementing.",
                "Always flag security issues (auth, input validation, API key handling, etc.).",
                "State reasons and trade-offs for all technical decisions.",
                "Include meaningful comments (the 'why') in all code.",
            ],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

    # ── AI/ML Dev / AIモデル開発 ──────────────────────────────────────
    "ai_ml": {
        "ja": {
            "role": (
                "あなたはMLシステムの研究から本番運用まで一貫して手がけてきたMLエンジニア兼リサーチャーです。"
                "論文実装・モデル選定・学習パイプライン構築・評価・本番デプロイの全工程に精通しています。"
                "再現性・実験管理・データの品質を最重視し、過学習やデータリークに対して常に警戒しています。"
                "最新の手法を把握しつつ、実務で本当に有効かどうかを批判的に評価します。"
            ),
            "fields": [
                ("language", "開発言語", "例: Python 3.11", True, [
                    "Python 3.11", "Python 3.10", "Python 3.9",
                    "R", "Julia", "Scala",
                ]),
                ("framework", "フレームワーク", "例: PyTorch / scikit-learn", False, [
                    "PyTorch",
                    "TensorFlow / Keras",
                    "scikit-learn",
                    "HuggingFace Transformers",
                    "LangChain / LlamaIndex",
                    "XGBoost / LightGBM",
                    "JAX",
                    "未定（提案してほしい）",
                ]),
                ("baseline", "既存モデル・ベースライン", "例: ロジスティック回帰F1=0.72", False, [
                    "なし（初回実装）",
                    "既存モデルあり（改善したい）",
                    "論文ベースの実装",
                    "他のフレームワークからの移植",
                ]),
                ("task_type", "タスク種別", "例: 二値分類 / 物体検出 / テキスト生成", False, [
                    "二値分類",
                    "多クラス分類",
                    "回帰",
                    "クラスタリング",
                    "テキスト分類（NLP）",
                    "固有表現抽出（NER）",
                    "テキスト生成・要約",
                    "画像分類（CV）",
                    "物体検出",
                    "セマンティックセグメンテーション",
                    "推薦システム",
                    "異常検知",
                    "時系列予測",
                    "RAG / LLM活用",
                ]),
                ("dataset", "データセット情報", "例: 表形式・10万件・不均衡比1:10", False, [
                    "表形式データ（均衡）",
                    "表形式データ（不均衡）",
                    "テキストデータ",
                    "画像データ",
                    "時系列データ",
                    "マルチモーダル（テキスト＋画像など）",
                    "データなし（設計段階）",
                ]),
                ("data_split", "データ分割・検証戦略", "例: Train/Val/Test=8:1:1・時系列CV", False, [
                    "Train/Val/Test = 8:1:1",
                    "Train/Val/Test = 7:2:1",
                    "K-fold CV (k=5)",
                    "Stratified K-fold",
                    "Time-series split",
                    "未定（提案してほしい）",
                ]),
                ("architecture", "アーキテクチャ・モデル", "例: BERT / ResNet / XGBoost", False, [
                    "未定（提案してほしい）",
                    "LightGBM / XGBoost",
                    "scikit-learn（ロジスティック回帰など）",
                    "BERT / RoBERTa",
                    "GPT系 / LLM（ファインチューニング）",
                    "ResNet / EfficientNet",
                    "Vision Transformer（ViT）",
                    "LSTM / GRU",
                    "Transformer（スクラッチ実装）",
                    "カスタムアーキテクチャ",
                ]),
                ("env", "学習環境", "例: MacBook MPS / Google Colab / AWS GPU", False, [
                    "MacBook（MPS / CPU）",
                    "Google Colab（GPU）",
                    "Linux（CUDA GPU）",
                    "AWS / GCP / Azure（クラウドGPU）",
                    "Docker コンテナ",
                ]),
                ("metric", "評価指標", "例: F1スコア / RMSE / AUC", False, [
                    "Accuracy",
                    "F1スコア（マクロ / マイクロ）",
                    "Precision / Recall",
                    "AUC-ROC",
                    "RMSE / MAE",
                    "BLEU / ROUGE",
                    "カスタム指標（説明を記載）",
                ]),
                ("serving_target", "推論要件・本番制約", "例: レイテンシ100ms以下 / 1日100万req", False, []),
                ("question", "質問・依頼内容", "例: モデルの精度が上がらない原因を教えてください", True, []),
                ("output_expectation", "期待する出力", "例: 原因分析＋改善策コード", False, [
                    "モデル設計・アーキテクチャ提案",
                    "学習パイプラインのコード",
                    "原因分析＋改善策",
                    "ハイパーパラメータチューニング戦略",
                    "評価・可視化コード",
                    "論文手法の実装",
                    "本番デプロイ設計",
                ]),
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
            ],
            "rules": [
                "データリーク・過学習のリスクがあれば必ず指摘してください。",
                "再現性確保のためにシード固定・実験管理の方法を含めてください。",
                "手法の選択には理由と想定される限界を明示してください。",
                "最新手法を提案する場合は実務での実績・信頼性についても言及してください。",
                "評価は訓練データではなく必ず検証・テストデータで行うよう強調してください。",
            ],
            "output_format": "",
            "lang_instruction": "必ず日本語で回答してください。",
        },
        "en": {
            "role": (
                "You are an ML engineer and researcher who has taken ML systems from research to production. "
                "You are proficient across the entire pipeline: paper implementation, model selection, training, evaluation, and deployment. "
                "You prioritize reproducibility, experiment management, and data quality above all. "
                "You are always on guard for overfitting and data leakage. "
                "You stay current with the latest methods while critically evaluating their real-world effectiveness."
            ),
            "fields": [
                ("language", "Programming language", "e.g. Python 3.11", True, [
                    "Python 3.11", "Python 3.10", "Python 3.9",
                    "R", "Julia", "Scala",
                ]),
                ("framework", "Framework", "e.g. PyTorch / scikit-learn", False, [
                    "PyTorch",
                    "TensorFlow / Keras",
                    "scikit-learn",
                    "HuggingFace Transformers",
                    "LangChain / LlamaIndex",
                    "XGBoost / LightGBM",
                    "JAX",
                    "Not decided (suggest one)",
                ]),
                ("baseline", "Existing model / baseline", "e.g. Logistic regression F1=0.72", False, [
                    "None (first implementation)",
                    "Existing model (want to improve)",
                    "Paper-based implementation",
                    "Porting from another framework",
                ]),
                ("task_type", "Task type", "e.g. Binary classification / Object detection / Text generation", False, [
                    "Binary classification",
                    "Multi-class classification",
                    "Regression",
                    "Clustering",
                    "Text classification (NLP)",
                    "Named entity recognition (NER)",
                    "Text generation / summarization",
                    "Image classification (CV)",
                    "Object detection",
                    "Semantic segmentation",
                    "Recommendation system",
                    "Anomaly detection",
                    "Time series forecasting",
                    "RAG / LLM application",
                ]),
                ("dataset", "Dataset info", "e.g. Tabular, 100k rows, imbalanced 1:10", False, [
                    "Tabular data (balanced)",
                    "Tabular data (imbalanced)",
                    "Text data",
                    "Image data",
                    "Time series data",
                    "Multimodal (text + image, etc.)",
                    "No data yet (design stage)",
                ]),
                ("data_split", "Data split / validation strategy", "e.g. Train/Val/Test=8:1:1, time-series CV", False, [
                    "Train/Val/Test = 8:1:1",
                    "Train/Val/Test = 7:2:1",
                    "K-fold CV (k=5)",
                    "Stratified K-fold",
                    "Time-series split",
                    "Not decided (suggest one)",
                ]),
                ("architecture", "Architecture / Model", "e.g. BERT / ResNet / XGBoost", False, [
                    "Not decided (suggest one)",
                    "LightGBM / XGBoost",
                    "scikit-learn (logistic regression, etc.)",
                    "BERT / RoBERTa",
                    "GPT-based / LLM (fine-tuning)",
                    "ResNet / EfficientNet",
                    "Vision Transformer (ViT)",
                    "LSTM / GRU",
                    "Transformer (from scratch)",
                    "Custom architecture",
                ]),
                ("env", "Training environment", "e.g. MacBook MPS / Google Colab / AWS GPU", False, [
                    "MacBook (MPS / CPU)",
                    "Google Colab (GPU)",
                    "Linux (CUDA GPU)",
                    "AWS / GCP / Azure (cloud GPU)",
                    "Docker container",
                ]),
                ("metric", "Evaluation metric", "e.g. F1 score / RMSE / AUC", False, [
                    "Accuracy",
                    "F1 score (macro / micro)",
                    "Precision / Recall",
                    "AUC-ROC",
                    "RMSE / MAE",
                    "BLEU / ROUGE",
                    "Custom metric (describe below)",
                ]),
                ("serving_target", "Serving constraints / production target", "e.g. <100ms latency / 1M req/day", False, []),
                ("question", "Question / Request", "e.g. Why is my model not improving?", True, []),
                ("output_expectation", "Expected output", "e.g. Root cause analysis + improved code", False, [
                    "Model design / architecture proposal",
                    "Training pipeline code",
                    "Root cause analysis + fixes",
                    "Hyperparameter tuning strategy",
                    "Evaluation & visualization code",
                    "Paper method implementation",
                    "Production deployment design",
                ]),
                ("notes", "Additional notes", "Any other context or special instructions", False, []),
            ],
            "rules": [
                "Always flag data leakage and overfitting risks.",
                "Include seed fixing and experiment tracking for reproducibility.",
                "State reasons and expected limitations for all method choices.",
                "When proposing recent methods, comment on their real-world reliability.",
                "Always emphasize evaluating on validation/test data, never training data.",
            ],
            "output_format": "",
            "lang_instruction": "Please respond in English.",
        },
    },

        # ── Other / その他 ─────────────────────────────────────────────
    "other": {
        "ja": {
            "role": (
                "あなたはこの質問・依頼の内容を読み、最もふさわしい専門家像を自ら設定してください。"
                "例えば、法律の質問なら「15年のキャリアを持つ弁護士」、"
                "ビジネスの質問なら「複数のスタートアップを経営した起業家」のように。"
                "スキル・経験・スタンスの3点を自ら定義し、その立場から一貫して回答してください。"
                "回答の冒頭で自分が設定した役割を1行で宣言してから始めてください。"
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
                ("notes", "備考・追記", "その他、AIへの補足や特記事項があれば", False, []),
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
                "Read this question/request and define the most fitting expert persona yourself. "
                "For example: for a legal question, 'a lawyer with 15 years of practice'; "
                "for a business question, 'an entrepreneur who has founded multiple startups'. "
                "Define your own skills, experience, and stance across 3 dimensions, then respond consistently from that perspective. "
                "Start your response by declaring in one line the role you have set for yourself."
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
                ("notes", "Additional notes", "Any other context or special instructions for the AI", False, []),
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

    # 3. 役割定義（カテゴリ固有の役割をベースに、視点を追加）
    role_label = "【役割】" if lang == "ja" else "【Role】"
    role_base = f"{role_label}\n{tmpl['role']}\n"

    # 役割の視点が選択されている場合のみ追加
    if role_perspectives and role_perspectives.strip():
        if lang == "ja":
            role_base += f"\nさらに以下の視点を加えて回答してください。\n- {role_perspectives.strip()}\n"
        else:
            role_base += f"\nAdditionally, respond from the following perspective(s):\n- {role_perspectives.strip()}\n"

    parts.append(role_base)

    # レシピカテゴリ：絶対的制約を役割の直後に挿入
    if category_key == "recipe":
        if lang == "ja":
            parts.append(
                "【絶対的制約】\n"
                "以下は回答の内容に関わらず必ず守ること。\n"
                "- プロフィールに登録された食材・調味料・調理器具・生活環境・食の好みを全て反映すること\n"
                "- 苦手な食材・避けたい食材は絶対に使わないこと（使う場合は代替案を必ず提示）\n"
                "- アレルギーは例外なく厳守すること\n"
                "- プロフィールの居住地・生活環境を考慮し、入手しやすい食材を優先すること\n"
                "- 材料の分量は必ず具体的な数値で記載すること\n"
            )
        else:
            parts.append(
                "【Absolute Constraints】\n"
                "The following must be observed regardless of the request.\n"
                "- Reflect all profile data: ingredients, condiments, tools, living environment, and food preferences\n"
                "- Never use disliked or avoided ingredients (if unavoidable, always offer substitutes)\n"
                "- Allergy restrictions must be followed without exception\n"
                "- Prioritize ingredients available in the user's location based on their profile\n"
                "- Always state ingredient quantities as specific numbers\n"
            )

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

    # レシピカテゴリは専用の自然言語形式で構築
    if category_key == "recipe":
        mode_val    = user_inputs.get("mode", "").strip()
        main_input  = user_inputs.get("main_input", "").strip()
        servings    = user_inputs.get("servings", "").strip()
        condition   = user_inputs.get("condition", "").strip()
        extra       = user_inputs.get("extra", "").strip()
        notes       = user_inputs.get("notes", "").strip()

        # モードごとの自然な依頼文
        mode_requests = {
            "ja": {
                "使い切り": (
                    f"今ある食材（{main_input}）を使い切るメニューを3案提案してください。"
                    "各案に「料理名 / 調理時間 / 使い切れる食材 / 一言ポイント」を記載し、"
                    "最もおすすめの1案については材料・分量・手順・プロのコツを含むフルレシピを提示してください。"
                ),
                "予算管理": (
                    f"予算・期間の条件（{main_input}）で献立を作成してください。"
                    "「曜日 / 料理名 / 概算コスト」の献立表と、"
                    "週1回の買い物で揃う食材リスト（食材名・量・目安金額）を作成し、"
                    "食材の使い回しで無駄が出ないよう工夫してください。"
                    "献立の中から1〜2品、代表的な料理の簡易レシピ（材料・手順）も提示してください。"
                ),
                "スキルアップ": (
                    f"「{main_input}」の作り方を教えてください。"
                    "まず完全なレシピ（材料・分量・手順）を提示した上で、"
                    "以下の構成でプロの解説を加えてください。"
                    "① なぜこの手順・技法なのか（調理科学の観点から）"
                    "② プロが意識しているコツ（初心者が見落としがちな点）"
                    "③ よくある失敗とその原因・対処法"
                    "④ 応用・バリエーションアイデア"
                ),
                "アイデア": (
                    f"条件・気分（{main_input}）に合う料理を3案提案してください。"
                    "各案に「料理名 / 調理時間 / なぜ今日この料理をおすすめするか / 難易度 / 簡易レシピ（材料・手順）」を記載してください。"
                    "プロのシェフならではの意外な視点も1案含めてください。"
                ),
                "作り置き": (
                    f"「{main_input}」をベースに週の食事準備を楽にする作り置きプランを作成してください。"
                    "各料理のフルレシピ（材料・分量・手順）と、"
                    "「保存方法・容器 / 日持ち / 週の使い回しアイデア（2〜3通り）」をセットで提示してください。"
                    "1〜2時間の調理で週の大半をカバーできるプランを目指してください。"
                ),
                "体調サポート": (
                    f"今日の体調・目標（{main_input}）を踏まえ、今日食べるべき料理を3案提案してください。"
                    "各案に「料理名 / 期待できる効果（栄養学的根拠1〜2文）/ 調理時間 / 注意点 / 簡易レシピ（材料・手順）」を記載してください。"
                ),
            },
            "en": {
                "Use it up": (
                    f"Suggest 3 recipe ideas to use up these ingredients: {main_input}. "
                    "For each: dish name / cooking time / ingredients used up / one-line highlight. "
                    "For the top recommended option, provide a full recipe with ingredients, quantities, steps, and a pro tip."
                ),
                "Budget plan": (
                    f"Create a meal plan given this budget/timeframe: {main_input}. "
                    "Include a meal table (day / dish name / estimated cost) and a shopping list "
                    "(ingredient / quantity / price). Plan ingredient reuse to minimize waste. "
                    "Also provide simple recipes (ingredients & steps) for 1-2 representative dishes."
                ),
                "Skill up": (
                    f"Please give me the full recipe for: {main_input}. "
                    "First provide the complete recipe (ingredients, quantities, steps), "
                    "then add a professional breakdown: "
                    "① Why this method (food science perspective) "
                    "② Pro tips beginners miss "
                    "③ Common mistakes, causes, fixes "
                    "④ Variations and applications."
                ),
                "Ideas": (
                    f"Suggest 3 recipe ideas based on: {main_input}. "
                    "For each: dish name / cooking time / why it fits today / difficulty / simple recipe (ingredients & steps). "
                    "Include at least one unexpected chef-inspired suggestion."
                ),
                "Meal prep": (
                    f"Design a meal prep plan around: {main_input}. "
                    "For each dish, provide a full recipe (ingredients, quantities, steps) plus: "
                    "storage method & container / shelf life / 2-3 reuse ideas during the week. "
                    "Target: completable in 1-2 hours, covering most of the week."
                ),
                "Health support": (
                    f"Based on today's condition/goal: {main_input} — "
                    "suggest 3 recipe options for today. "
                    "For each: dish name / expected benefits (1-2 sentences of nutritional rationale) / cooking time / cautions / simple recipe (ingredients & steps)."
                ),
            },
        }

        fmt_map = mode_requests.get(lang, mode_requests["ja"])
        request_text = None

        # まずlangのキーでマッチ試行、次にja/enのキーでも試みる（UI言語とlang設定が異なる場合の対応）
        for key, text in fmt_map.items():
            if key in mode_val:
                request_text = text
                break

        # マッチしなかった場合、反対言語のキーで試みる
        if not request_text:
            fallback_lang = "ja" if lang == "en" else "en"
            fallback_map = mode_requests.get(fallback_lang, {})
            for key, text in fallback_map.items():
                if key in mode_val:
                    # fallbackで見つかったキーに対応する、本来のlangのテキストを使用
                    ja_keys = list(mode_requests["ja"].keys())
                    en_keys = list(mode_requests["en"].keys())
                    try:
                        if fallback_lang == "ja":
                            idx = ja_keys.index(key)
                            request_text = mode_requests[lang][en_keys[idx]]
                        else:
                            idx = en_keys.index(key)
                            request_text = mode_requests[lang][ja_keys[idx]]
                    except (ValueError, KeyError, IndexError):
                        request_text = text
                    break

        if request_text:
            input_lines.append(request_text)
        elif main_input:
            input_lines.append(main_input)

        if servings:
            input_lines.append(f"- {'人数' if lang == 'ja' else 'Servings'}: {servings}")
        if condition:
            input_lines.append(f"- {'今日の状態' if lang == 'ja' else 'Today'}: {condition}")
        if extra:
            input_lines.append(f"- {'補足' if lang == 'ja' else 'Note'}: {extra}")
        if notes:
            input_lines.append(f"- {'備考' if lang == 'ja' else 'Additional'}: {notes}")

    else:
        # 通常カテゴリ：フィールドラベルと値をそのまま使用
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

        # カテゴリ固有の出力構造ヒントを依頼内容に追加
        output_hints = {
            "ai_pm": {
                "ja": "回答は「状況整理 → 選択肢（A/B/C）のメリット・デメリット・推奨条件 → 主なリスク」の順で整理してください。",
                "en": "Structure your response as: Situation summary → Options (A/B/C) with pros, cons, and recommended conditions → Key risks.",
            },
            "code": {
                "ja": "回答は「実装コード → 使用例 → テストコード（pytest形式）→ 注意点・改善案」の順で出力してください。",
                "en": "Output in this order: Implementation code → Usage example → Test code (pytest style) → Notes & improvements.",
            },
            "app_dev": {
                "ja": "回答は「要件の整理・確認事項 → 設計方針・技術選定の理由 → 実装コード（主要部分）→ セキュリティ上の注意点 → 改善案」の順で出力してください。",
                "en": "Structure your response as: Requirements & clarifications → Design approach & tech rationale → Implementation code (key parts) → Security considerations → Improvement suggestions.",
            },
            "ai_ml": {
                "ja": "回答は「問題の分析・仮説 → 提案手法と選定理由 → 実装コード → データリーク・過学習リスクの注意点 → 評価方法・次のステップ」の順で出力してください。",
                "en": "Structure your response as: Problem analysis & hypothesis → Proposed approach with rationale → Implementation code → Data leakage & overfitting risks → Evaluation method & next steps.",
            },
            "health": {
                "ja": "レシピを含む場合は「材料（分量付き）→ カロリー概算 → 手順（所要時間付き）→ 栄養バランスのポイント → アレンジ案2つ」の形式で出力してください。",
                "en": "If a recipe is included, use this structure: Ingredients (with quantities) → Estimated calories → Steps (with time) → Nutrition highlights → 2 variation ideas.",
            },
            "study": {
                "ja": "回答は「直感的な説明 → 具体例 → 正式な定義・数式 → よくある誤解 → 理解確認の小問（2問）→ 次に学ぶべきトピック」の順で出力してください。",
                "en": "Structure your response as: Intuitive explanation → Concrete example → Formal definition & formulas → Common misconceptions → Quick check questions (x2) → What to study next.",
            },
            "language": {
                "ja": "回答は「今日のテーマ → 重要表現・単語（例文付き）→ 練習問題 → よくある間違いと注意点 → 次のステップ」の順で出力してください。",
                "en": "Structure your response as: Today's theme → Key expressions & vocabulary (with examples) → Practice exercises → Common mistakes & tips → Next steps.",
            },
            "chat": {
                "ja": "会話形式で返答してください。練習目的の場合は返答の最後に【フィードバック】セクションを追加し、改善点や良かった点を簡潔に伝えてください。",
                "en": "Respond in dialogue format. For practice purposes, add a [Feedback] section at the end with brief notes on what was good and what could be improved.",
            },
            "other": {
                "ja": "回答の冒頭で、あなたが設定した役割（専門家像）を1行で宣言してから回答を始めてください。",
                "en": "Start your response with a one-line declaration of the expert role you have set for yourself, then proceed with your answer.",
            },
        }
        hint = output_hints.get(category_key, {}).get(lang)
        if hint:
            input_lines.append(f"- {hint}")


    if input_lines:
        parts.append("【質問・依頼内容】" if lang == "ja" else "【Request】")
        parts.extend(input_lines)

    # 6. 出力ルール（制約・品質基準のみ）
    out_label = "【出力ルール】" if lang == "ja" else "【Output Rules】"
    out_lines = [f"- {rule}" for rule in tmpl["rules"]]

    # 通常カテゴリは output_format をそのまま使用（レシピは制約のみなので不要）
    if category_key != "recipe":
        for line in tmpl["output_format"].splitlines():
            line = line.strip()
            if line:
                out_lines.append(f"- {line}" if not line.startswith("-") else line)

    out_lines.append(f"- {tmpl['lang_instruction']}")
    parts.append(f"\n{out_label}\n" + "\n".join(out_lines))

    return "\n".join(parts)
