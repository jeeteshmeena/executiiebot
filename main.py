import os
import asyncio
import threading
from flask import Flask
from pyrogram import Client, idle
from pyrogram.errors import FloodWait


# =========================
# Environment variables
# =========================

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


# =========================
# Telegram Bot
# =========================

bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# =========================
# Flask health server
# =========================

web = Flask(__name__)

@web.route("/")
def home():
    return "ExecutiieBot is running"


def run_web():
    port = int(os.getenv("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


# =========================
# Bot runner
# =========================

async def run_bot():

    while True:

        try:

            await bot.start()

            print("✅ Bot connected to Telegram")

            await idle()

            await bot.stop()

        except FloodWait as e:

            wait_time = int(e.value)

            print(f"⚠ FloodWait detected. Sleeping {wait_time} seconds")

            await asyncio.sleep(wait_time)

        except Exception as err:

            print("❌ Bot crashed:", err)

            await asyncio.sleep(10)


# =========================
# Main
# =========================

if __name__ == "__main__":

    print("🚀 ExecutiieBot starting...")

    # run Flask health server
    threading.Thread(target=run_web).start()

    # run Telegram bot
    asyncio.run(run_bot())
