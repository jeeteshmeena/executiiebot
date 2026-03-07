from pyrogram import Client, filters

ABOUT_TEXT = """
🎭 <b>About</b>

🤖 <b>ExecutiieBot</b> — Story Media Assistant

📡 <a href="https://t.me/MeJeetX">@MeJeetX</a>

<b>Admin:</b> <a href="https://t.me/MeJeetX">JeetX</a>

<b>Host:</b> Render  
<b>Database:</b> MongoDB

<i>Version: V1.0</i>
"""

@Client.on_message(filters.command("about"))
async def about_handler(client, message):

    await message.reply_text(
        ABOUT_TEXT,
        parse_mode="html",
        disable_web_page_preview=True
    )
