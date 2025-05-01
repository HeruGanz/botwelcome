from pyrogram import Client, filters
import time

start_time = time.time()

@Client.on_message(filters.command("status") & filters.me)
async def uptime(client, message):
    uptime = time.time() - start_time
    hours, remainder = divmod(int(uptime), 3600)
    minutes, seconds = divmod(remainder, 60)
    await message.reply(f"⏱ Uptime: {hours} jam {minutes} menit {seconds} detik")
