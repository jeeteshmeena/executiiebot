
from pyrogram import filters
from database.mongo import stories

def register_search(bot):
    @bot.on_message(filters.text & ~filters.command(["start","help","stories","latest","request"]))
    async def search(client, message):
        query = message.text.strip().lower()
        data = await stories.find_one({"story_name": {"$regex": query, "$options": "i"}})
        if not data:
            await message.reply_text("Story not found.")
            return
        total = data.get("total", 0)
        await message.reply_text(
            f"📖 {data['story_name']}\nEpisodes: {total}\n"
            "Use range like 1-100."
        )
