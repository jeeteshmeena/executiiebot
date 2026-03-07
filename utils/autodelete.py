import asyncio

async def delete_later(message, delay=300):
    try:
        await asyncio.sleep(delay)
        await message.delete()
    except:
        pass
