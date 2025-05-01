from pyrogram import Client, filters
from pyrogram.types import Message

APPROVED = set()

@Client.on_message(filters.command("approve") & filters.me)
async def approve_pm(client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else None
    if user_id:
        APPROVED.add(user_id)
        await message.reply("✅ Pengguna disetujui.")

@Client.on_message(filters.private & ~filters.me)
async def auto_block(client, message: Message):
    if message.from_user.id not in APPROVED:
        await message.reply("⛔ Maaf, kamu tidak diizinkan mengirim pesan.")
        await client.block_user(message.from_user.id)
