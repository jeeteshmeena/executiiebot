from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.mongo import stories

@Client.on_message(filters.text & ~filters.command(["start","help","about","latest","stories","request"]))
async def search(client, message):

    query = message.text.strip()

    story = await stories.find_one({"title":{"$regex":query,"$options":"i"}})

    if not story:

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔎 Google Search", url=f"https://www.google.com/search?q={query}"),
                InlineKeyboardButton("📩 Contact Admin", url="https://t.me/MeJeetX")
            ]
        ])

        text = f"""
<b>{query}</b>

❗️ <b>File Not Found</b>

📝 <i>Check the spelling or try searching with the exact title.</i>
"""

        await message.reply_text(text, reply_markup=buttons)
