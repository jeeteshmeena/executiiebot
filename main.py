import os
import threading
from flask import Flask
from pyrogram import Client, filters

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


# =====================
# REGISTER HANDLERS
# =====================

register_start(bot)
register_help(bot)
register_about(bot)
register_request(bot)
register_latest(bot)
register_stories(bot)
register_range(bot)
register_story_select(bot)

print("✅ Handlers loaded")


# =====================
# HEALTH SERVER (Render)
# =====================

app = Flask(__name__)


@app.route("/")
def home():
    return "ExecutiieBot running"


def run_web():
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# =====================
# BOT START
# =====================

@bot.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("🏓 Bot alive")


async def startup():

    print("🤖 Bot connected")

    try:
        await index_channel(bot)
        print("📚 Channel indexed")
    except Exception as e:
        print("Index error:", e)


if __name__ == "__main__":

    threading.Thread(target=run_web).start()

    bot.run(startup())
