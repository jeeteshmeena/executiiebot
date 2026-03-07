from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.mongo import episodes

def register_story_select(app):

    @app.on_callback_query()
    async def story_select(client, query):

        if not query.data.startswith("story"):
            return

        story = query.data.split("|")[1]

        total = await episodes.count_documents({"story": story})

        ranges = []
        start = 1

        while start <= total:
            end = min(start + 99, total)
            ranges.append((start, end))
            start += 100

        buttons = []

        for i in range(0, len(ranges), 2):

            row = []

            r1 = ranges[i]

            row.append(
                InlineKeyboardButton(
                    f"{r1[0]}-{r1[1]}",
                    callback_data=f"range|{story}|{r1[0]}|{r1[1]}"
                )
            )

            if i + 1 < len(ranges):

                r2 = ranges[i+1]

                row.append(
                    InlineKeyboardButton(
                        f"{r2[0]}-{r2[1]}",
                        callback_data=f"range|{story}|{r2[0]}|{r2[1]}"
                    )
                )

            buttons.append(row)

        await query.message.reply_text(
            f"📚 <b>{story}</b>\nEpisodes: <b>{total}</b>",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
