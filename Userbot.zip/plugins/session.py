from pyrogram import Client, filters

@Client.on_message(filters.command("session") & filters.me)
async def check_session(client, message):
    me = await client.get_me()
    await message.reply(f"🔐 Session aktif sebagai: {me.first_name} (@{me.username})")
