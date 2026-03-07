import os
import asyncio
import threading
from flask import Flask
from pyrogram import Client

from handlers.start import register_start
from handlers.help import register_help
from handlers.stories import register_stories
from handlers.search import register_search
from handlers.latest import register_latest
from handlers.request import register_request
from handlers.range import register_range

from indexer.channel_indexer import register_indexer


asyncio.set_event_loop(asyncio.new_event_loop())


app = Flask(__name__)

@app.route("/")
def home():
    return "ExecutiieBot running"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")


bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


def main():

    register_start(bot)
    register_help(bot)
    register_stories(bot)
    register_search(bot)
    register_latest(bot)
    register_request(bot)
    register_range(bot)

    register_indexer(bot)

    print("ExecutiieBot started")

    bot.run()


if __name__ == "__main__":

    threading.Thread(target=run_web).start()

    main()
