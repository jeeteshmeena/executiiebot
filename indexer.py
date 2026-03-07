from pyrogram import Client
from db import episodes
import re

CHANNEL_ID = -100xxxxxxxxxx

async def index_channel(bot: Client):

    async for msg in bot.get_chat_history(CHANNEL_ID):

        if msg.audio or msg.document or msg.voice:

            text = msg.caption or ""

            match = re.search(r"(.*)\s+Episode\s+(\d+)", text, re.I)

            if not match:
                continue

            story = match.group(1).strip()
            ep = int(match.group(2))

            file_id = None

            if msg.audio:
                file_id = msg.audio.file_id
            elif msg.document:
                file_id = msg.document.file_id
            elif msg.voice:
                file_id = msg.voice.file_id

            if not file_id:
                continue

            await episodes.update_one(
                {"story": story, "episode": ep},
                {
                    "$set": {
                        "story": story,
                        "episode": ep,
                        "file_id": file_id,
                        "msg_id": msg.id
                    }
                },
                upsert=True
            )

            print(f"Indexed {story} episode {ep}")
