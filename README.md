# 🧠 AI Options Trading Bot (Django + MongoDB + Telegram)

This is a full-stack Django app using AI indicators (RSI, EMA, Supertrend, Harmonics) to generate trade signals on indexes like Nifty, BankNifty, etc.

---

## 🚀 Features

- MongoDB-based Django backend
- JWT login (username/password → access token)
- Strategy logic (XABCD, RSI, EMA, Supertrend)
- Telegram alerts with strike, SL, target
- Render-ready deployment
- Breakeven SL adjustment
- Multi-index support (BankNifty, Nifty, etc.)

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/Satkar/ai-options-trader.git
cd ai-options-trader


python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


cp .env.example .env
