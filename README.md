# 📈 BIST Stock Alert Bot (Telegram)

A cloud-ready Python bot that tracks **BIST stocks** in real time via **TradingView** and sends **Telegram alerts** when target prices or stop-loss levels are reached.

Designed to run 24/7 on platforms like **Render**, with built-in spam protection and error handling.

---

****  on the other hand you can alter your following stock list on the code 

## 🚀 Features

- 📊 Real-time price tracking via TradingView Scanner API  
- 🔔 Telegram notifications for:
  - Target price breakout
  - Stop-loss (lower limit) breakdown
- 🧠 Smart alert locking (prevents spam messages)
- 🌐 Flask health-check endpoint for cloud hosting
- 🔁 Automatic retry & rate-limit handling (HTTP 429)
- ☁️ Cloud-friendly (Render / Heroku style deployment)

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **Telegram Bot API**
- **TradingView Scanner API**
- `requests`, `threading`

---

## ⚙️ Environment Variables 



The following environment variables must be set:


BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id


📋 Tracked Stock Configuration

Stocks are defined with:

Cost price

Target price

Stop-loss level

example output 
{
  "ad": "THYAO",
  "maliyet": 273.3,
  "hedef": 340.0,
  "alt_limit": 307.0
}

-------  Running Locally
pip install -r requirements.txt
python app.py


The bot starts automatically in a background thread.


Author
Halil İbrahim Mutlu
Electrical & Electronics Engineer
