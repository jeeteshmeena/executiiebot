import os
import asyncio
import threading

from pyrogram import Client, idle
from flask import Flask

# handlers
from handlers.start import register_start
from handlers.help import register_help
from handlers.about import register_about
from handlers.request import register_request
from handlers.latest import register_latest
from handlers.stories import register_stories
from handlers.range import register_range
from handlers.story_select import register_story_select


# environment variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")


# telegram bot
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


print("ExecutiieBot started")


# flask health server
web = Flask(__name__)

@web.route("/")
def home():
    return "ExecutiieBot is running"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


async def run_bot():
    await bot.start()
    print("Bot connected to Telegram")
    await idle()
    await bot.stop()


if __name__ == "__main__":

    # start flask in background
    threading.Thread(target=run_web).start()

    # start telegram bot
    asyncio.run(run_bot())
