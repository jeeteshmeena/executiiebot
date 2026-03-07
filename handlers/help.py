from pyrogram import Client, filters

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

@Client.on_message(filters.command("help"))
async def help_handler(client, message):

    await message.reply_text(
        HELP_TEXT,
        parse_mode="html"
    )
