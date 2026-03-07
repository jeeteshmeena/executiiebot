from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from utils.cleanup import auto_delete

WELCOME = """
✨ <b>Welcome!</b>

ExecutiieBot — Story Audio Index Bot
"""

def register_start(app):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message):

        buttons = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Channel", url="https://t.me/MeJeetX"),
                InlineKeyboardButton("Group", url="https://t.me/+HvKfFsPziO42OTNl")
            ]]
        )

        msg = await message.reply_text(
            WELCOME,
            parse_mode="html",
            reply_markup=buttons
        )

        try:
            await message.delete()
        except:
            pass

        asyncio.create_task(
            auto_delete(client, message.chat.id, [msg.id], 600)
        )
