from pyrogram import filters
import asyncio
from utils.cleanup import auto_delete


HELP_TEXT = """
📚 <b>Search Help</b>

<b>Stories:</b>
<i>Story Name</i>
Example → <code>Yakshini</code>

<b>Episode search:</b>
<i>Story Name Episode Number</i>
Example → <code>Yakshini 12</code>

<b>Tip:</b>
<i>Add keywords like episode / part</i>

🍿 <b>Send your query now!</b>
"""


def register_help(app):

    @app.on_message(filters.command("help"))
    async def help_handler(client, message):

        msg = await message.reply_text(
            HELP_TEXT,
            parse_mode="html"
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
