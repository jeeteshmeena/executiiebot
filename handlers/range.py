from pyrogram import filters
from database.mongo import episodes

def register_range(bot):

    @bot.on_callback_query(filters.regex("range_"))

    async def send_range(client, query):

        data = query.data.split("_")

        start = int(data[1])
        end = int(data[2])

        eps = episodes.find(
            {"episode_start": {"$lte": end}, "episode_end": {"$gte": start}}
        )

        async for ep in eps:

            await query.message.reply_audio(ep["file_id"])
