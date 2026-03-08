from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import episodes


def register_search(bot):

    @bot.on_message(filters.text & ~filters.command(["start", "help", "stories", "latest", "about", "request"]))
    async def search_handler(client, message):

        query = message.text.strip()

        story = await episodes.find_one({
            "story": {"$regex": f"^{query}$", "$options": "i"}
        })

        if not story:
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔎 Search on Google",
                            url=f"https://www.google.com/search?q={query}+story"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "📩 Contact Admin",
                            url="https://t.me/MeJeetX"
                        )
                    ]
                ]
            )

            await message.reply_text(
                "❗️ **File Not Found**\n\n"
                "📝 Check the spelling or try searching with the exact title.",
                reply_markup=buttons
            )
            return

        await message.reply_text(
            f"📚 **{query} found!**\n\nUse /stories to view episodes."
        )
