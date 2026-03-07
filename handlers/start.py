
from pyrogram import filters

def register_start(bot):
    @bot.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply_text(
            "✨ Welcome to ExecutiieBot!\n\n"
            "Use /stories to see available stories."
        )
