import re
import os
from database.mongo import episodes

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))


async def index_channel(bot):

    try:
        # first resolve the chat
        chat = await bot.get_chat(CHANNEL_ID)
        print(f"Connected to channel: {chat.title}")

    except Exception as e:
        print("Channel access error:", e)
        return

    try:

        async for msg in bot.get_chat_history(chat.id):

            if not (msg.audio or msg.document or msg.voice):
                continue

            caption = msg.caption or ""

            match = re.search(r"(.*)\s+Episode\s+(\d+)", caption, re.I)

            if not match:
                continue

            story = match.group(1).strip()
            episode = int(match.group(2))

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
                {"story": story, "episode": episode},
                {
                    "$set": {
                        "story": story,
                        "episode": episode,
                        "file_id": file_id,
                        "msg_id": msg.id
                    }
                },
                upsert=True
            )

            print(f"Indexed {story} episode {episode}")

    except Exception as e:
        print("History read error:", e)
