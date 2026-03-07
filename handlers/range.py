from pyrogram import Client
from pyrogram.types import CallbackQuery
from database.mongo import episodes


@Client.on_callback_query()
async def send_range(client, query: CallbackQuery):

    data = query.data.split("|")

    story = data[1]
    start = int(data[2])
    end = int(data[3])

    eps = episodes.find({
        "story": story,
        "episode": {"$gte": start, "$lte": end}
    })

    async for ep in eps:
        await query.message.reply_audio(ep["file_id"])
