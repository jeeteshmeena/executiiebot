import os
import asyncio
import threading

from flask import Flask
from pyrogram import Client, idle
from pyrogram.errors import FloodWait

from handlers.start import register_start
from handlers.help import register_help
from handlers.about import register_about
from handlers.request import register_request
from handlers.latest import register_latest
from handlers.stories import register_stories
from handlers.range import register_range
from handlers.story_select import register_story_select

from indexer import index_channel


API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


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


def run_web():
    port = int(os.getenv("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


async def run_bot():

    while True:

        try:

            await bot.start()

            print("Bot connected to Telegram")

            await index_channel(bot)

            print("Channel indexing complete")

            await idle()

            await bot.stop()

        except FloodWait as e:

            wait_time = int(e.value)

            print(f"FloodWait: waiting {wait_time} seconds")

            await asyncio.sleep(wait_time)

        except Exception as err:

            print("Bot crashed:", err)

            await asyncio.sleep(10)


if __name__ == "__main__":

    print("Starting ExecutiieBot...")

    threading.Thread(target=run_web).start()

    asyncio.run(run_bot())
