from pyrogram import Client, filters

@Client.on_message(filters.group & filters.text & ~filters.me)
async def anti_link(client, message):
    if "t.me/" in message.text or "telegram.me/" in message.text:
        await message.delete()
