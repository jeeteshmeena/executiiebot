from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import episodes


def register_range(bot: Client):

    @bot.on_callback_query(filters.regex("^range_"))
    async def send_range(client, query):

        data = query.data.split("_")

        story = data[1]
        start = int(data[2])
        end = int(data[3])

        await query.answer()

        # strict story filter + episode sorting
        eps = []

        async for ep in episodes.find(
            {
                "story": story,
                "episode": {"$gte": start, "$lte": end}
            }
        ).sort("episode", 1):

            eps.append(ep)

        if not eps:
            await query.message.reply_text("No episodes found.")
            return

        for ep in eps:

            file_id = ep["file_id"]

            try:

                await query.message.reply_audio(file_id)

            except Exception:

                await query.message.reply_document(file_id)
