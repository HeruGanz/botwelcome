from pyrogram import Client, filters

@Client.on_message(filters.command("alive") & filters.me)
async def alive(client, message):
    await message.reply("✅ **Userbot aktif!**
Versi: 1.0
By: @YourUsername")
