# Slack WhatsApp Copy Generator (/copygen)

This is a simple Slack app with a `/copygen` slash command that takes a brief and returns 3 WhatsApp-ready marketing copy options using OpenAI GPT-4.

## Features

- Supports Portuguese 🇧🇷 and Spanish 🇪🇸
- Adapts to location and seasonality (inferred from prompt)
- Adds emojis 😎 (emojis count as 2 characters)
- Keeps responses under 1024 characters

## Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Set your OpenAI API Key

Set the environment variable:

**On Linux/macOS:**
```
export OPENAI_API_KEY=your-api-key-here
```

**On Windows:**
```
set OPENAI_API_KEY=your-api-key-here
```

### 3. Run the server

```
python main.py
```

The server will start on port 3000.

### 4. Slack Integration

- Create a new Slack app at https://api.slack.com/apps
- Add a **Slash Command** `/copygen` pointing to: `https://yourdomain.com/slack`
- Add `commands` and `chat:write` to **OAuth scopes**
- Install the app in your workspace

You're done! 🎉