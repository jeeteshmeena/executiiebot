from pyrogram import Client, filters
from db import episodes
from datetime import datetime, timedelta


def register_latest(bot: Client):

    @bot.on_message(filters.command("latest"))
    async def latest_handler(client, message):

        since = datetime.utcnow() - timedelta(hours=24)

        stories = []

        async for ep in episodes.find(
            {"created_at": {"$gte": since}}
        ):

            if ep["story"] not in stories:
                stories.append(ep["story"])

        if not stories:

            await message.reply_text(
                "📢 No new uploads in last 24 hours."
            )
            return

        text = "**📢 Here are the latest uploads!**\n\n"

        for i, s in enumerate(stories, 1):

            text += f"{i}. {s}\n"

        await message.reply_text(text)
