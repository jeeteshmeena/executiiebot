from pyrogram import filters
from database.mongo import stories
from datetime import datetime, timedelta
import asyncio
from utils.cleanup import auto_delete

def register_latest(app):

    @app.on_message(filters.command("latest"))
    async def latest_handler(client, message):

        since = datetime.utcnow() - timedelta(hours=24)

        cursor = stories.find({
            "updated_at": {"$gte": since}
        })

        names = []

        async for s in cursor:
            names.append(s["title"])

        if not names:

            text = """
📢 <b>Here are the latest uploads!</b>

<i>No new stories uploaded in the last 24 hours.</i>
"""

        else:

            story_list = "\n".join(
                [f"{i+1}. {n}" for i, n in enumerate(names)]
            )

            text = f"""
📢 <b>Here are the latest uploads!</b>

🆕 <b>We've gathered the newest releases for you.</b>

{story_list}
"""

        msg = await message.reply_text(text, parse_mode="html")

        try:
            await message.delete()
        except:
            pass

        asyncio.create_task(
            auto_delete(client, message.chat.id, [msg.id], 600)
        )
