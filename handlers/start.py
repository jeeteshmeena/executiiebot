from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_handler(client, message):

    text = """
✨ <b>Welcome, {}</b>

<b>𝗘𝘅𝗲𝗰𝘂𝘁𝗶𝗶𝗕𝗼𝘁 — Audio Story Search Bot 🤖</b>

<b>Commands:</b> /latest • /help • /request • /about • /stories

<b>Disclaimer 📌</b>
<i>We only index Telegram files. We do not host content.</i>

<u>Send your query to begin!</u>

<a href="https://t.me/MeJeetX">📢 Channel</a> | <a href="https://t.me/+HvKfFsPziO42OTNl">💬 Group</a>
""".format(message.from_user.first_name)

    await message.reply_text(text)
