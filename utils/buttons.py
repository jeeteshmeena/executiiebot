from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_range_buttons(total):

    buttons = []

    start = 1

    while start <= total:

        end = min(start + 99, total)

        buttons.append(
            [InlineKeyboardButton(f"{start}-{end}", callback_data=f"range_{start}_{end}")]
        )

        start = end + 1

    return InlineKeyboardMarkup(buttons)
