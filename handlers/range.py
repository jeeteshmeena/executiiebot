from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from database.mongo import episodes


async def send_range(client: Client, query: CallbackQuery):

    try:
        data = query.data.split("|")

        story = data[1]
        start = int(data[2])
        end = int(data[3])

        eps = episodes.find({
            "story": story,
            "episode": {"$gte": start, "$lte": end}
        }).sort("episode", 1)

        async for ep in eps:

            file_id = ep["file_id"]

            # AUDIO send
            await query.message.reply_audio(file_id)

    except Exception as e:
        print(e)


def register_range(app: Client):

    @app.on_callback_query(filters.regex("^range"))
    async def range_handler(client, query: CallbackQuery):
        await send_range(client, query)
