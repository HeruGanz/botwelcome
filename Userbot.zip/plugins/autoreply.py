from pyrogram import Client, filters

@Client.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    await message.reply("Hai! Ini adalah balasan otomatis dari userbot.")
