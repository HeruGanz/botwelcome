from pyrogram import Client, filters
from pyrogram.types import Message

AFK_MODE = False
AFK_REASON = ""

@Client.on_message(filters.command("afk") & filters.me)
async def set_afk(client, message: Message):
    global AFK_MODE, AFK_REASON
    AFK_REASON = " ".join(message.command[1:]) or "AFK"
    AFK_MODE = True
    await message.reply(f"🔕 Kamu sekarang AFK: {AFK_REASON}")

@Client.on_message(filters.private & ~filters.me)
async def auto_reply_afk(client, message: Message):
    if AFK_MODE:
        await message.reply(f"Saya sedang AFK: {AFK_REASON}")

@Client.on_message(filters.command("back") & filters.me)
async def unset_afk(client, message: Message):
    global AFK_MODE
    AFK_MODE = False
    await message.reply("✅ Kamu sudah kembali dari AFK.")
