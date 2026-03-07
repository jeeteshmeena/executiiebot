import re
from pyrogram import filters
from database.models import add_story, add_episode

current_story = None
episode_counter = 1

def register_indexer(bot):

    @bot.on_message(filters.channel)
    async def index_channel(client, message):
        global current_story, episode_counter

        # STORY POSTER
        if message.photo and message.caption and "Episodes -" in message.caption:

            caption = message.caption

            title_line = caption.split("\n")[0]

            story = title_line.split("|")[0].strip()
            platform = title_line.split("|")[1].strip()

            total = int(re.search(r"(\d+)", caption).group())

            current_story = story
            episode_counter = 1

            await add_story(story, platform, total)

            return

        # STORY END
        if message.text and "Story Completed" in message.text:
            current_story = None
            return

        # EPISODE FILE
        if message.audio or message.document or message.video:

            if not current_story:
                return

            filename = ""

            if message.audio:
                filename = message.audio.file_name or ""

            if message.document:
                filename = message.document.file_name or ""

            # RANGE DETECTION (31-40)
            match = re.search(r"(\d+)-(\d+)", filename)

            if match:
                start = int(match.group(1))
                end = int(match.group(2))
            else:
                # SINGLE EPISODE
                num = re.search(r"(\d+)", filename)

                if num:
                    start = int(num.group(1))
                    end = start
                else:
                    start = episode_counter
                    end = episode_counter

            episode_counter = end + 1

            file_id = (
                message.audio.file_id if message.audio else
                message.document.file_id if message.document else
                message.video.file_id
            )

            await add_episode(current_story, start, end, file_id)
