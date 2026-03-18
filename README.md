# 🤖 AI Prompt Builder

**A personal AI assistant with structured prompt engineering — Gemini & OpenAI supported**

> A portfolio project by **Manami Oyama** | AI Engineer / Data Scientist  
> Built for CPT job search (Data Science / AI Engineering roles)

---

## 📌 What is this?

AI Prompt Builder is a **full-stack web application** that generates structured, role-aware prompts for AI models across multiple domains — AI/PM strategy, code, recipe, health, language learning, and more.

Instead of typing raw questions into ChatGPT, this app:
- Assigns an **expert role** to the AI (e.g., Senior PM at Google, nutritionist)
- Injects your **personal profile** (tech stack, dietary preferences, learning goals)
- Structures the request with domain-specific **output rules**
- Supports **Gemini and OpenAI** models interchangeably

---

## 🎯 Why This Project

This project demonstrates the **PM × AI Engineering** skill set:

| Skill | Demonstrated by |
|---|---|
| **Prompt engineering** | Structured multi-section prompts with role, context, rules |
| **LLM integration** | Dual-provider support (Gemini + OpenAI) with fallback logic |
| **Full-stack Python** | Flask REST API + vanilla JS frontend |
| **Product thinking** | User profile persistence, presets, favorites, history |
| **Bilingual UX** | Full Japanese / English language switching |
| **Docker deployment** | Containerized for production-ready portability |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│         Browser (index.html)        │
│   Vanilla JS — no framework         │
└────────────────┬────────────────────┘
                 │ REST API
┌────────────────▼────────────────────┐
│         Flask (main.py)             │
│   20+ API endpoints                 │
└──┬──────────┬───────────┬───────────┘
   │          │           │
┌──▼──┐  ┌───▼───┐  ┌────▼────────┐
│gemini│  │storage│  │ templates   │
│client│  │  .py  │  │    .py      │
│ .py  │  │       │  │             │
└──┬───┘  └───────┘  └─────────────┘
   │
┌──▼──────────────────┐
│  Gemini / OpenAI API │
└──────────────────────┘
```

---

## ✨ Features

### 10 Prompt Categories
| Category | Expert Role Assigned |
|---|---|
| AI-PM | Senior PM (10+ AI products shipped at Google) |
| Code | Senior full-stack engineer (15+ years) |
| App Dev | Full-stack AI/DS engineer |
| AI/ML Dev | Senior ML researcher |
| Health & Life | Registered dietitian + personal trainer |
| Study | University professor + tutor |
| Language | Native speaker + language coach |
| Chat | Conversation partner |
| Recipe | Professional chef (Michelin-trained) |
| Other | Auto-assigned domain expert |

### Prompt Customization
- **Simple / Detailed mode** toggle
- **Role perspective** selection (e.g., as a beginner / expert)
- **Context history** injection (continue a previous conversation)
- **Custom instructions** (e.g., "answer concisely", "show reasoning")

### Persistence
- **Profile**: Personal info per category (tech stack, diet, learning goals)
- **Presets**: Save and reload field combinations per category
- **Favorites**: Star prompts for reuse
- **History**: Last 100 Q&A pairs with search

### LLM Support
- **Gemini**: `gemini-2.5-flash`, `gemini-2.5-pro`, `gemini-2.0-flash`
- **OpenAI**: `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `gpt-3.5-turbo`
- API keys managed in UI settings (never hardcoded)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.12 / Flask |
| **Frontend** | Vanilla JS / HTML / CSS (no framework) |
| **LLM** | Google Gemini API / OpenAI API |
| **Storage** | JSON files (file-based, no database) |
| **Deployment** | Docker + Gunicorn |
| **i18n** | Custom dictionary-based (Japanese / English) |

---

## 📁 File Structure

```
ai-prompt-builder/
├── main.py               # Flask app + 20+ REST endpoints
├── gemini_client.py      # LLM abstraction (Gemini + OpenAI)
├── storage.py            # JSON-based persistence layer
├── templates.py          # Prompt templates + build_prompt()
├── templates/
│   └── index.html        # Single-page frontend (vanilla JS)
├── settings_example.json # Config template (commit this)
├── settings.json         # Config with API keys (gitignored)
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Local (without Docker)

```bash
git clone https://github.com/your-username/ai-prompt-builder.git
cd ai-prompt-builder
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy and configure settings:
```bash
cp settings_example.json settings.json
# Edit settings.json and add your API key
```

Run:
```bash
python main.py
# Opens http://127.0.0.1:5001 automatically
```

### Docker

```bash
docker build -t ai-prompt-builder .
docker run -p 5001:5001 \
  -e GEMINI_API_KEY=your-key-here \
  ai-prompt-builder
```

---

## 🔒 Security Notes

- **Never commit `settings.json`** — it contains API keys
- `settings.json` is gitignored; use `settings_example.json` as template
- API keys can also be set via environment variable `GEMINI_API_KEY`
- The UI settings panel lets users input their own API keys at runtime

---

## 📦 Requirements

```
flask
google-genai
python-dotenv
openai
gunicorn
```

---

## 👩‍💻 About the Author

**Manami Oyama**  
AI Engineer / Data Scientist / PM  
📍 Honolulu, Hawaii  
🎓 KCC (CPT eligible)

- 4 years Data Science
- 2 years AI Engineering
- 3 years Web Development

Currently seeking CPT part-time positions in Data Science / AI Engineering.

MIT License
