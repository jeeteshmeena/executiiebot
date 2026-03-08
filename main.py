import asyncio
import os
from flask import Flask
from pyrogram import Client, idle
from pyrogram.errors import FloodWait

from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import register_start
from handlers.help import register_help
from handlers.stories import register_stories
from handlers.search import register_search
from handlers.range import register_range
from handlers.latest import register_latest
from handlers.about import register_about
from handlers.request import register_request
from indexer import index_channel


app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "ExecutiieBot is running"


bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


async def run_bot():

    # Register handlers
    register_start(bot)
    register_help(bot)
    register_stories(bot)
    register_search(bot)
    register_range(bot)
    register_latest(bot)
    register_about(bot)
    register_request(bot)

    await bot.start()
    print("Bot connected to Telegram")

    # Start indexing in background
    asyncio.create_task(index_channel(bot))
    print("Channel indexing started")

    await idle()


def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)


async def main():
    await run_bot()


if __name__ == "__main__":
    print("ExecutiieBot started")

    loop = asyncio.get_event_loop()

    # Run flask in separate thread
    import threading
    threading.Thread(target=run_flask).start()

    while True:
        try:
            loop.run_until_complete(main())
        except FloodWait as e:
            print(f"FloodWait: waiting {e.value} seconds")
            loop.run_until_complete(asyncio.sleep(e.value))
        except Exception as e:
            print("Bot error:", e)
            loop.run_until_complete(asyncio.sleep(10))
