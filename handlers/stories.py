from pyrogram import filters
from database.mongo import stories

def register_stories(bot):

    @bot.on_message(filters.command("stories"))

    async def stories_list(client, message):

        text = "📚 Available Stories\n\n"

        i = 1

        async for s in stories.find():

            text += f"{i}. {s['story_name']}\n"

            i += 1

        await message.reply_text(text)
