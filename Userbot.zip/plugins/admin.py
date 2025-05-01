from pyrogram import Client, filters

@Client.on_message(filters.command("ban") & filters.me)
async def ban_user(client, message):
    if message.reply_to_message:
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("🚫 Pengguna dibanned.")

@Client.on_message(filters.command("unban") & filters.me)
async def unban_user(client, message):
    if message.reply_to_message:
        await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("✅ Pengguna diunban.")
