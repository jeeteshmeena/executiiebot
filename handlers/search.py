from pyrogram import filters
from database.mongo import stories
from utils.buttons import create_range_buttons

def register_search(bot):

    @bot.on_message(filters.text & ~filters.command(["start","help","stories","latest","request"]))
    async def search(client, message):

        query = message.text.lower()

        story = await stories.find_one({
            "story_name": {"$regex": query, "$options": "i"}
        })

        if not story:
            return

        total = story["total"]

        keyboard = create_range_buttons(total)

        await message.reply_text(
            f"📖 {story['story_name']} | {story['platform']}\n"
            f"Episodes: {total}",
            reply_markup=keyboard
        )
