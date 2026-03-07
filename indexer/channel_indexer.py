import re
import os
from pyrogram import filters
from database.models import add_story, add_episode

DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL"))

current_story = None
episode_counter = 1

def register_indexer(bot):

    @bot.on_message(filters.chat(DATABASE_CHANNEL))
    async def index_channel(client, message):

        global current_story
        global episode_counter

        # STORY POSTER DETECTION
        if message.photo and message.caption and "Episodes -" in message.caption:

            caption = message.caption

            try:
                first_line = caption.split("\n")[0]

                story_name = first_line.split("|")[0].strip()
                platform = first_line.split("|")[1].strip()

                total = int(re.search(r"(\d+)", caption).group())

                current_story = story_name
                episode_counter = 1

                await add_story(story_name, platform, total)

                print(f"Indexed story: {story_name}")

            except Exception as e:
                print("Poster parse error:", e)

            return


        # STORY COMPLETED
        if message.text and "Story Completed" in message.text:

            print("Story completed:", current_story)

            current_story = None
            episode_counter = 1
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

            # RANGE DETECT (31-40)
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

            print(f"Indexed episode {start}-{end} for {current_story}")
