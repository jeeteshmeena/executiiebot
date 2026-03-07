from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.mongo import stories

NOT_FOUND = """
❗️ <b>File Not Found</b>

📝 <i>Check the spelling or try searching with the exact title.</i>
"""

@Client.on_message(filters.text & ~filters.command(["start","help","about","request","latest","stories"]))
async def search(client, message):

    query = message.text.strip()

    story = await stories.find_one({
        "title": {"$regex": query, "$options": "i"}
    })

    if not story:

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔎 Google Search",
                        url=f"https://www.google.com/search?q={query}+story+audio"
                    ),
                    InlineKeyboardButton(
                        "📩 Contact Admin",
                        url="https://t.me/MeJeetX"
                    )
                ]
            ]
        )

        await message.reply_text(
            NOT_FOUND,
            parse_mode="html",
            reply_markup=buttons
        )
        return
