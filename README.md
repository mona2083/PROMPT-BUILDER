# 🤖 AI Prompt Builder

> Stop writing prompts from scratch every time. Use structured templates, your personal profile, and AI optimization to generate expert-level prompts instantly.

A Flask web app that transforms the way you interact with AI — by building context-rich, role-specific prompts tailored to your profile, expertise, and goals.

---

## Live Demo

🔗 [Open App](http://138.68.47.65:8083/)

---

## The Problem It Solves

Most people type a one-line question into ChatGPT or Gemini and get a generic answer. The quality of AI output is almost entirely determined by the quality of the prompt — and most prompts are missing:

- **Role definition** — who should the AI be? (A 30-year chef? A senior ML engineer? A polyglot language coach?)
- **User context** — what do you know, where do you live, what tools do you have?
- **Constraints** — what are the non-negotiables? (allergies, coding language, deadline)
- **Output structure** — in what format should the answer come?

This app solves all of that automatically, by combining your saved profile with category-specific templates to generate prompts that would take a human expert 10 minutes to write by hand.

---

## The 10 Prompt Categories

| Category | Expert Role | Best For |
|---|---|---|
| 🤖 AI-PM | Senior PM with 10+ AI product launches | AI project decisions, risk, roadmap |
| 💻 Code | Senior ML Engineer, 5+ yrs production | Functions, debugging, refactoring |
| 📱 App Dev | Full-stack engineer, 10+ yrs | Web/mobile/API app design & implementation |
| 🧠 AI/ML Dev | ML Engineer + Researcher | Model design, training pipeline, evaluation |
| 🌿 Health & Life | Certified Sports Nutritionist + Trainer | Diet, exercise, lifestyle habits |
| 📚 Study | Academic coach, PhD, 1,000+ students | University courses, deep understanding |
| 🌍 Language | Polyglot, 7 languages, 1,000+ learners | Conversation, grammar, exam prep |
| 💬 Chat | Persona embodiment coach | Roleplay, language practice, interview prep |
| 🍳 Recipe | Pro chef + culinary researcher, 30+ yrs | Cooking coaching, meal planning, skill-up |
| ✨ Other | Self-defined expert | Any topic not covered above |

---

## Features

### 🧬 Personal Profile System
- **5 profile groups**: Common / Tech / Life & Health / Cooking & Food / Study & Language
- Saved once, auto-injected into every relevant prompt
- Toggle on/off per prompt generation
- Custom fields per group (e.g. "I usually keep rice and pasta at home", "Living in Hawaii")

### 🎭 Role & Perspective System
- Each category has a deeply defined expert role (skills + experience + stance)
- Optional **Role Perspective** overlay: Expert / Critical Reviewer / User View / Technical / Business / Teacher
- Multiple perspectives can be combined for multi-angle output

### 📋 Structured Prompt Architecture
Every generated prompt follows a deliberate structure:
```
【Instructions & Rules】   ← User-selected rules (AI reads this first)
【User Profile】           ← Auto-injected from saved profile
【Role】                   ← Category-specific expert definition
【Absolute Constraints】   ← Recipe category: allergies, dislikes (non-negotiable)
【Request】                ← Your inputs + mode-specific detailed instruction
【Output Rules】           ← Language, format, quality constraints
```

### 🍳 Recipe Coaching Modes
The Recipe category goes far beyond "suggest a recipe":

| Mode | What it does |
|---|---|
| 🥗 Use it up | 3 menu ideas from your current ingredients + full recipe for top pick |
| 💰 Budget plan | Weekly meal table + shopping list within your budget |
| 📚 Skill up | Full recipe first, then food-science explanation + pro tips |
| 💡 Ideas | 3 ideas matching your mood/condition + simple recipe for each |
| 🥣 Meal prep | Bulk cooking plan + storage + weekly reuse ideas |
| 🏥 Health support | 3 recipes based on today's condition + nutritional rationale |

### 🤖 AI Optimization
- Generate a prompt, then click **"Optimize with AI"** to have an AI prompt engineer rewrite it
- The Role and Request sections are improved; your Rules and Profile are preserved
- Switch between **Template** and **AI Optimized** tabs to compare

### 💾 Preset System
- Save any combination of inputs as a named preset per category
- Restore in one click for recurring tasks

### 🔧 Instructions & Rules
- 6 built-in rule presets: General / Accuracy / Reasoning / Code / Language / Format
- Select multiple presets simultaneously
- Add custom rules and save them

### 📜 History & Favorites
- Every prompt is auto-saved to history
- Star any prompt to save to Favorites
- Reload prompts from either list

### 🌐 Bilingual (JA / EN)
- Full Japanese / English toggle — UI, prompts, and AI instructions all switch
- Works mid-session

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python / Flask |
| Frontend | Vanilla HTML + CSS + JavaScript (single file) |
| AI Providers | Google Gemini API / OpenAI API (switchable) |
| Storage | Local JSON files (history, profile, presets, favorites) |
| Deployment | Render / Railway (Procfile included) |

---

## How the Prompt Engine Works

The core engine lives in `templates.py` → `build_prompt()`:

1. **Profile injection** — loads the relevant profile groups for the category and formats them as labeled key-value pairs
2. **Role construction** — pulls the category's expert role definition; appends selected perspectives
3. **Constraint layer** — for Recipe, injects `【Absolute Constraints】` block (allergies, dislikes)
4. **Request assembly** — for Recipe categories, constructs a natural-language request from the selected mode and inputs; for other categories, uses field labels and values plus an output structure hint
5. **Rules compilation** — assembles category rules + output format + language instruction

The result is a prompt that a professional prompt engineer would write — without the user needing to think about any of it.

---

## Project Structure

```
prompt_builder/
├── main.py              # Flask server — all API endpoints
├── templates.py         # Prompt templates + build_prompt() engine
├── gemini_client.py     # Gemini / OpenAI API client
├── storage.py           # JSON persistence — profile, history, presets
├── requirements.txt
├── Procfile             # web: gunicorn main:app
└── templates/
    └── index.html       # Full frontend (single file)
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- A Google Gemini API key (free) or OpenAI API key

### Installation

```bash
git clone https://github.com/mona2083/prompt-builder.git
cd prompt-builder
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Open [http://localhost:5001](http://localhost:5001) in your browser.

### First Run
On first launch, a setup screen will appear. You can either:
- Enter a **Gemini or OpenAI API key** to enable AI features
- Click **"Use without API key"** to use prompt generation only (no AI sending)

> API keys are stored in your browser's `localStorage` only — they are never sent to or stored on the server.

---

## Usage

### Quick Start
1. Select a **category tab** (e.g. Recipe, Code, AI-PM)
2. Fill in the form fields — required fields are marked in red
3. Click **"Generate Prompt"** — the structured prompt appears on the right
4. Copy it and paste into ChatGPT, Gemini, or any AI tool

### Profile Setup (Recommended)
Click **"Profile"** in the header and fill in your details once:
- **Common**: Name, age, occupation, native language, preferred answer style
- **Tech**: OS, programming language, experience, dev tools, rules
- **Cooking & Food**: Living environment, food preferences, dislikes, allergies, pantry staples, kitchen tools
- **Life & Health**: Lifestyle, hobbies, health goals
- **Study & Language**: Major, level, target language, study style

Your profile is automatically injected into every prompt.

### AI Features
- Check **"Send to AI and get answer"** to submit the prompt and receive a response in-app
- Check **"Optimize prompt with AI"** to have an AI rewrite your prompt before sending

---

## Deployment

### Hosted demo: server default API keys (`settings.json`)

For a **portfolio / public demo**, you can put Gemini / OpenAI keys in **`settings.json`** on the server (or set **`GEMINI_API_KEY`** in the environment). The web UI will:

- **Skip the first-run API key wizard** when those defaults exist
- Use **server keys** for `/api/ask_ai` whenever the visitor leaves key fields empty (local overrides still win if they paste their own key in Settings)

> **Security:** Anyone who can open your site can potentially extract keys from network responses or abuse your quota. Use a **restricted / quota-capped** key for demos, or keep keys client-only for untrusted audiences.

### Render (Recommended)
1. Push to a public GitHub repository
2. Go to [render.com](https://render.com) 
3. Connect your repo and configure:

| Setting | Value |
|---|---|
| Runtime | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn main:app` |
| Instance Type | Free |

4. Click **"Create Web Service"**

> API keys can be client-side only, or set on the server for a hosted demo — see [Hosted demo](#hosted-demo-server-default-api-keys-settingsjson) above.

### Railway
1. Push to GitHub
2. Go to [railway.app](https://railway.app) → **New Project → Deploy from GitHub**
3. Railway auto-detects the `Procfile` and deploys

---

## Author

**Manami Oyama** — AI Engineer / Product Manager  
🌺 Honolulu, Hawaii  
🔗 [Portfolio](https://mona2083.github.io/portfolio-2026/index.html) | [GitHub](https://github.com/mona2083) | [LinkedIn](https://www.linkedin.com/in/manami-oyama/)

---
