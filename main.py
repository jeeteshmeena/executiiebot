import os
import asyncio
from pyrogram import Client
from flask import Flask

from handlers.start import register_start
from handlers.help import register_help
from handlers.about import register_about
from handlers.request import register_request
from handlers.latest import register_latest
from handlers.stories import register_stories
from handlers.range import register_range
from handlers.story_select import register_story_select

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_start(bot)
register_help(bot)
register_about(bot)
register_request(bot)
register_latest(bot)
register_stories(bot)
register_range(bot)
register_story_select(bot)

print("ExecutiieBot started")

web = Flask(__name__)

@web.route("/")
def home():
    return "ExecutiieBot is running"


async def main():
    await bot.start()
    print("Bot connected to Telegram")
    from pyrogram import idle
await idle()


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    import threading

    def run_web():
        web.run(host="0.0.0.0", port=port)

    threading.Thread(target=run_web).start()

    asyncio.run(main())
