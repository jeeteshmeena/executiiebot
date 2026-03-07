import os
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


app = Client(
    "executiiebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


register_start(app)
register_help(app)
register_about(app)
register_request(app)
register_latest(app)
register_stories(app)
register_range(app)
register_story_select(app)


print("ExecutiieBot started")


web = Flask(__name__)

@web.route("/")
def home():
    return "ExecutiieBot is running"


if __name__ == "__main__":
    app.start()

    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)
