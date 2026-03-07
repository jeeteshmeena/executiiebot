
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def range_buttons(total):
    buttons = []
    start = 1
    while start <= total:
        end = min(start+99, total)
        buttons.append([InlineKeyboardButton(f"{start}-{end}", callback_data=f"{start}-{end}")])
        start = end+1
    return InlineKeyboardMarkup(buttons)
