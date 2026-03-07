import os
import threading
from flask import Flask
from pyrogram import Client

# Handlers
from handlers.start import register_start
from handlers.help import register_help
from handlers.stories import register_stories
from handlers.search import register_search
from handlers.latest import register_latest
from handlers.request import register_request
from handlers.range import register_range

# Indexer
from indexer.channel_indexer import register_indexer

# Flask server for Render
app = Flask(__name__)

@app.route("/")
def home():
    return "ExecutiieBot is running"

def run_web():
    app.run(host="0.0.0.0", port=10000)


# Telegram API credentials
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Create bot client
bot = Client(
    "ExecutiieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


def main():

    # Register command handlers
    register_start(bot)
    register_help(bot)
    register_stories(bot)
    register_search(bot)
    register_latest(bot)
    register_request(bot)

    # Register episode range buttons
    register_range(bot)

    # Register channel indexer
    register_indexer(bot)

    print("ExecutiieBot started successfully")

    bot.run()


if __name__ == "__main__":

    # Start Flask web server
    threading.Thread(target=run_web).start()

    # Start Telegram bot
    main()
