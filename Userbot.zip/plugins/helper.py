from pyrogram import Client, filters

@Client.on_message(filters.command("help") & filters.me)
async def helper(client, message):
    text = "**Daftar Perintah:**
"
    text += "/alive - Cek status bot
"
    text += "/afk <alasan> - Aktifkan mode AFK
"
    text += "/back - Kembali dari AFK
"
    text += "/approve - Izinkan PM
"
    text += "/ban - Ban user (balas pesan)
"
    text += "/unban - Unban user (balas pesan)
"
    text += "/broadcast <teks> - Kirim ke semua chat
"
    text += "/massdm <teks> - Kirim ke semua PM
"
    await message.reply(text)
