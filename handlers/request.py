
from pyrogram import filters
from database.mongo import requests

def register_request(bot):
    @bot.on_message(filters.command("request"))
    async def request_story(client, message):
        text = message.text.replace("/request","").strip()
        if not text:
            await message.reply_text("Please provide story name.")
            return
        await requests.insert_one({"story": text})
        await message.reply_text("✅ Request submitted.")
