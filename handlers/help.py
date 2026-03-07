
from pyrogram import filters

def register_help(bot):
    @bot.on_message(filters.command("help"))
    async def help_handler(client, message):
        text = (
            "📖 Help\n\n"
            "Send a story name to search.\n"
            "Example: Vashikaran\n"
            "You will get episode ranges."
        )
        await message.reply_text(text)
