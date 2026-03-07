
from pyrogram import filters
from database.mongo import stories
import datetime

def register_latest(bot):
    @bot.on_message(filters.command("latest"))
    async def latest_handler(client, message):
        day = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
        data = stories.find({"created_at": {"$gte": day}})
        text = "🆕 Latest Stories\n\n"
        async for s in data:
            text += f"{s['story_name']}\n"
        await message.reply_text(text)
