
from pyrogram import filters
from database.mongo import stories

def register_stories(bot):
    @bot.on_message(filters.command("stories"))
    async def list_stories(client, message):
        data = stories.find()
        text = "📚 Available Stories\n\n"
        i = 1
        async for s in data:
            text += f"{i}. {s['story_name']}\n"
            i += 1
        if i == 1:
            text += "No stories found."
        await message.reply_text(text)
