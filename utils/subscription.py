async def check_sub(client, user, channels):

    for ch in channels:

        member = await client.get_chat_member(ch, user)

        if member.status == "left":
            return False

    return True
