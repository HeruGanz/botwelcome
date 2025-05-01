from pyrogram import Client, filters

@Client.on_message(filters.all)
async def log_all(client, message):
    print(f"[{message.chat.id}] {message.from_user.first_name}: {message.text}")
