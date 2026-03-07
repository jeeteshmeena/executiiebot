from pyrogram import Client, filters
from db import episodes


def register_range(bot: Client):

    @bot.on_callback_query(filters.regex("^range_"))
    async def send_range(client, query):

        data = query.data.split("_")

        story = data[1]
        start = int(data[2])
        end = int(data[3])

        await query.answer()

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

            try:
                await query.message.reply_audio(ep["file_id"])
            except Exception:
                await query.message.reply_document(ep["file_id"])
