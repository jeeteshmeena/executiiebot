from database.mongo import episodes
from utils.cleanup import auto_delete
import asyncio

def register_range(app):

    @app.on_callback_query()
    async def range_handler(client, query):

        if not query.data.startswith("range"):
            return

        data = query.data.split("|")

        story = data[1]
        start = int(data[2])
        end = int(data[3])

        eps = episodes.find({
            "story": story,
            "episode": {"$gte": start, "$lte": end}
        }).sort("episode", 1)

        sent = []

        async for ep in eps:

            m = await query.message.reply_audio(ep["file_id"])
            sent.append(m.id)

        asyncio.create_task(auto_delete(
            client,
            query.message.chat.id,
            sent,
            21600
        ))
