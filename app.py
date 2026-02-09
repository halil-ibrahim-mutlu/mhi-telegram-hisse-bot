import os
import threading
import time
import random
import requests
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route("/")
def home():
    return "BOT CALISIYOR", 200


def telegram_mesaj(metin):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": metin,
        "parse_mode": "Markdown"
    }
    try:
        r = requests.post(url, data=payload, timeout=10)
        if r.status_code != 200:
            print("Telegram hata:", r.text)
    except Exception as e:
        print("Telegram exception:", e)


def tum_fiyatlari_cek(semboller):
    url = "https://scanner.tradingview.com/turkey/scan"
    payload = {
        "symbols": {
            "tickers": [f"BIST:{s}" for s in semboller],
            "query": {"types": []}
        },
        "columns": ["close"]
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code != 200:
            return {}

        data = r.json()
        fiyatlar = {}

        for item in data["data"]:
            symbol = item["s"].split(":")[1]
            fiyatlar[symbol] = item["d"][0]

        return fiyatlar

    except:
        return {}


takipler = [
    {"ad": "KOPOL", "hedef": 6.48, "alt_limit": 5.73},
    {"ad": "QUAGR", "hedef": 2.75, "alt_limit": 2.61},
]


def bot_loop():
    semboller = [h["ad"] for h in takipler]
    telegram_mesaj("🤖 Bot Render üzerinde başladı!")

    while True:
        fiyatlar = tum_fiyatlari_cek(semboller)

        for hisse in takipler:
            ad = hisse["ad"]
            fiyat = fiyatlar.get(ad)

            if fiyat is None:
                continue

            if fiyat >= hisse["hedef"]:
                telegram_mesaj(f"🎯 HEDEF AŞILDI: {ad} → {fiyat} TL")

            elif fiyat <= hisse["alt_limit"]:
                telegram_mesaj(f"⚠️ ALT LİMİT KIRILDI: {ad} → {fiyat} TL")

        time.sleep(random.randint(45, 65))


threading.Thread(target=bot_loop, daemon=True).start()
