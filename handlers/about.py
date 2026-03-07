from pyrogram import filters
import asyncio
from utils.cleanup import auto_delete

ABOUT_TEXT = """
🎭 <b>About</b>

🤖 <b>ExecutiieBot</b>

Admin: @MeJeetX  
Host: Render  
Database: MongoDB
"""

def register_about(app):

    @app.on_message(filters.command("about"))
    async def about_handler(client, message):

        msg = await message.reply_text(
            ABOUT_TEXT,
            parse_mode="html"
        )

        try:
            await message.delete()
        except:
            pass

        asyncio.create_task(
            auto_delete(client, message.chat.id, [msg.id], 600)
        )
