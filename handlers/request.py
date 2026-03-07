from pyrogram import Client, filters
from utils.cleanup import auto_delete
import asyncio

REQUEST_CHANNEL = -1003714374498

OK = """
✅ <b>Your request has been submitted!</b>
"""

NEED = """
🎬 <b>Please provide the name of story</b>

📝 <b>Examples:</b>
<code>/request Yakshini</code>
<code>/request Saaya A Cursed Love Story</code>
"""

@Client.on_message(filters.command("request"))
async def request_handler(client, message):

    cmd = message.id

    text = message.text.split(maxsplit=1)

    if len(text) == 1:

        m = await message.reply_text(NEED, parse_mode="html")

        await message.delete()

        asyncio.create_task(auto_delete(
            client,
            message.chat.id,
            [m.id],
            600
        ))

        return

    story = text[1]

    await client.send_message(
        REQUEST_CHANNEL,
        f"📩 Request\nUser: {message.from_user.mention}\nStory: {story}"
    )

    m = await message.reply_text(OK, parse_mode="html")

    await message.delete()

    asyncio.create_task(auto_delete(
        client,
        message.chat.id,
        [m.id],
        600
    ))
