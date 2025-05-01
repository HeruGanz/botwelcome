from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("massdm") & filters.me)
async def mass_dm(client, message: Message):
    text = " ".join(message.command[1:])
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "private":
            try:
                await client.send_message(dialog.chat.id, text)
            except:
                continue
    await message.reply("📤 Mass DM selesai.")
