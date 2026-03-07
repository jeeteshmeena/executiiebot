from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import episodes


def register_stories(bot: Client):

    @bot.on_message(filters.command("stories"))
    async def stories_list(client, message):

        stories = await episodes.distinct("story")

        if not stories:
            await message.reply_text("No stories found.")
            return

        buttons = []

        for s in stories:

            buttons.append([
                InlineKeyboardButton(
                    s,
                    callback_data=f"story_{s}"
                )
            ])

        await message.reply_text(
            "📚 Available Stories",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
