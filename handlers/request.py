from pyrogram import Client, filters

REQUEST_OK = """
✅ <b>Your request has been submitted!</b>
"""

REQUEST_NEED = """
🎬 <b>Please provide the name of story</b>

📝 <b>Examples:</b>
<code>/request Yakshini</code>
<code>/request Saaya A Cursed Love Story</code>
"""

@Client.on_message(filters.command("request"))
async def request_handler(client, message):

    text = message.text.split(maxsplit=1)

    if len(text) == 1:

        await message.reply_text(
            REQUEST_NEED,
            parse_mode="html"
        )
        return

    story = text[1]

    await message.reply_text(
        REQUEST_OK,
        parse_mode="html"
    )
