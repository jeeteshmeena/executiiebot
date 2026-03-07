
# Simple helper functions for database operations
from .mongo import stories, episodes

async def add_story(name, platform, total):
    await stories.update_one(
        {"story_name": name},
        {"$set": {"story_name": name, "platform": platform, "total": total}},
        upsert=True
    )

async def add_episode(story, start, end, file_id):
    await episodes.insert_one({
        "story": story,
        "episode_start": start,
        "episode_end": end,
        "file_id": file_id
    })
