import os
import asyncio
import threading

from flask import Flask
from pyrogram import Client, idle

# handlers
from handlers.start import register_start
from handlers.help import register_help
from handlers.about import register_about
from handlers.request import register_request
from handlers.latest import register_latest
from handlers.stories import register_stories
from handlers.range import register_range
from handlers.story_select import register_story_select

# indexer
from indexer import index_channel


print("🚀 ExecutiieBot starting...")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# register handlers
register_start(bot)
register_help(bot)
register_about(bot)
register_request(bot)
register_latest(bot)
register_stories(bot)
register_range(bot)
register_story_select(bot)


print("ExecutiieBot handlers loaded")


# Flask health server for Render
app = Flask(__name__)


@app.route("/")
def home():
    return "ExecutiieBot running"


def run_web():
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


async def run_bot():

    await bot.start()

    print("🤖 Bot connected to Telegram")

    try:
        await index_channel(bot)
        print("📚 Channel indexing complete")
    except Exception as e:
        print("Index error:", e)

    print("✅ Bot is now running")

    await idle()


def start():

    threading.Thread(target=run_web).start()

    asyncio.run(run_bot())


if __name__ == "__main__":

    start()
