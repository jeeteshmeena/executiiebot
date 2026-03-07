
async def check_subscription(client, user_id, channels):
    for ch in channels:
        member = await client.get_chat_member(ch, user_id)
        if member.status == "left":
            return False
    return True
