from pyrogram import Client, filters

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    for user in message.new_chat_members:
        await message.reply(f"👋 Selamat datang, {user.mention}!")
