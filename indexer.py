import re
from db import episodes

# यहाँ अपना database channel id डालो
CHANNEL_ID = -1003714374498


async def index_channel(bot):

    async for msg in bot.get_chat_history(CHANNEL_ID):

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
