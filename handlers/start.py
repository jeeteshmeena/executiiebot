from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.cleanup import auto_delete
import asyncio


WELCOME_TEXT = """
✨ <b>Welcome, {name}!</b>

<u><b>ExecutiieBot — Story Audio Index Bot</b></u> 🤖

<b>Commands:</b> /latest • /help • /request • /about • /stories

<b>Disclaimer 📌</b>
<i>We only index Telegram files. We do not host content.</i>

<b>Send your story name to begin!</b>

<a href="https://t.me/MeJeetX">@MeJeetX</a>
"""


def register_start(app):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message):

        name = message.from_user.first_name if message.from_user else "Friend"

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⭐ Channel ⭐",
                        url="https://t.me/MeJeetX"
                    ),
                    InlineKeyboardButton(
                        "⚡ Group ⚡",
                        url="https://t.me/+HvKfFsPziO42OTNl"
                    )
                ]
            ]
        )

        msg = await message.reply_text(
            WELCOME_TEXT.format(name=name),
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=buttons
        )

        await message.delete()

        asyncio.create_task(
            auto_delete(
                client,
                message.chat.id,
                [msg.id],
                600
            )
        )
