from pyrogram import Client
from pyrogram.types import CallbackQuery
from database.mongo import episodes
from utils.cleanup import auto_delete
import asyncio

async def send_range(client: Client, query: CallbackQuery):

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

def register_range(app: Client):

    @app.on_callback_query()
    async def range_handler(client, query: CallbackQuery):
        if query.data.startswith("range"):
            await send_range(client, query)
