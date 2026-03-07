from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import episodes


def register_story_select(bot: Client):

    @bot.on_callback_query(filters.regex("^story_"))
    async def story_selected(client, query):

        story = query.data.split("_", 1)[1]

        await query.answer()

        total = await episodes.count_documents({"story": story})

        if total == 0:
            await query.message.reply_text("No episodes found.")
            return

        ranges = []

        start = 1

        while start <= total:

            end = start + 99

            if end > total:
                end = total

            ranges.append((start, end))

            start += 100

        buttons = []

        row = []

        for r in ranges:

            row.append(
                InlineKeyboardButton(
                    f"{r[0]}-{r[1]}",
                    callback_data=f"range_{story}_{r[0]}_{r[1]}"
                )
            )

            if len(row) == 2:
                buttons.append(row)
                row = []

        if row:
            buttons.append(row)

        await query.message.reply_text(
            f"🎧 {story} Episodes",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
