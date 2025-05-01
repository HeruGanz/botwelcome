from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("broadcast") & filters.me)
async def broadcast(client, message: Message):
    text = " ".join(message.command[1:])
    async for dialog in client.get_dialogs():
        try:
            await client.send_message(dialog.chat.id, text)
        except:
            continue
    await message.reply("✅ Pesan berhasil disiarkan.")
