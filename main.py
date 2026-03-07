import os
import asyncio
import threading

from flask import Flask
from pyrogram import Client
from pyrogram import idle


API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")


bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# Flask health server (Render requirement)
app = Flask(__name__)

@app.route("/")
def home():
    return "ExecutiieBot Running"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


async def run_bot():
    await bot.start()
    print("Bot connected to Telegram")
    await idle()
    await bot.stop()


if __name__ == "__main__":

    # run flask server
    threading.Thread(target=run_web).start()

    # run bot
    asyncio.run(run_bot())
