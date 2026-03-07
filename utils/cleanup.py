import asyncio

async def auto_delete(client, chat_id, message_ids, delay):
    await asyncio.sleep(delay)
    try:
        await client.delete_messages(chat_id, message_ids)
    except:
        pass
