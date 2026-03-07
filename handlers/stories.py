from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.mongo import stories
from utils.cleanup import auto_delete
import asyncio

TEXT = """
📚 <b>Available Stories</b>

<i>Select a story below to explore episodes.</i>
"""

@Client.on_message(filters.command("stories"))
async def stories_handler(client, message):

    cmd = message.id

    data = stories.find().sort("title", 1)

    buttons = []

    async for s in data:
        buttons.append(
            [InlineKeyboardButton(
                f"📖 {s['title']}",
                callback_data=f"story|{s['title']}"
            )]
        )

    msg = await message.reply_text(
        TEXT,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    await message.delete()

    asyncio.create_task(auto_delete(
        client,
        message.chat.id,
        [msg.id],
        600
    ))
