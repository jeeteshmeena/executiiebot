
from pyrogram import filters
from database.models import add_story, add_episode
import re

current_story = None
episode_counter = 1

def register_indexer(bot):

    @bot.on_message(filters.channel)
    async def index_channel(client, message):
        global current_story, episode_counter

        if message.photo and message.caption and "Episodes -" in message.caption:
            lines = message.caption.split("\n")
            title = lines[0]
            total = int(re.search(r"(\d+)", message.caption).group())
            story = title.split("|")[0].strip()
            platform = title.split("|")[1].strip()
            current_story = story
            episode_counter = 1
            await add_story(story, platform, total)

        elif message.text and "Story Completed" in message.text:
            current_story = None

        elif message.audio or message.document or message.video:
            if current_story:
                name = message.caption or message.audio.file_name if message.audio else ""
                rng = re.search(r"(\d+)-(\d+)", str(name))
                if rng:
                    start = int(rng.group(1))
                    end = int(rng.group(2))
                else:
                    start = episode_counter
                    end = episode_counter
                    episode_counter += 1
                file_id = (
                    message.audio.file_id if message.audio else
                    message.document.file_id if message.document else
                    message.video.file_id
                )
                await add_episode(current_story, start, end, file_id)
