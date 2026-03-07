from pyrogram import filters
import asyncio
from utils.cleanup import auto_delete


ABOUT_TEXT = """
🎭 <b>About</b>

🤖 <b>ExecutiieBot</b> — Story Media Assistant

📡 <a href="https://t.me/MeJeetX">@MeJeetX</a>

<b>Admin:</b> <a href="https://t.me/MeJeetX">JeetX</a>

<b>Host:</b> Render  
<b>Database:</b> MongoDB

<i>Version: V1.0</i>
"""


def register_about(app):

    @app.on_message(filters.command("about"))
    async def about_handler(client, message):

        msg = await message.reply_text(
            ABOUT_TEXT,
            parse_mode="html",
            disable_web_page_preview=True
        )

        try:
            await message.delete()
        except:
            pass

        asyncio.create_task(
            auto_delete(
                client,
                message.chat.id,
                [msg.id],
                600
            )
        )
