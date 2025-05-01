
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, SESSION_NAME

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, message: Message):
    await message.edit("Pong!")

@app.on_message(filters.command("hello", prefixes=".") & filters.me)
async def hello(_, message: Message):
    await message.edit("Hai! Saya userbot aktif.")

@app.on_message(filters.command("me", prefixes=".") & filters.me)
async def whoami(client, message: Message):
    user = await client.get_me()
    await message.edit(f"👤 Username: @{user.username}\n🆔 ID: `{user.id}`")

if __name__ == "__main__":
    print("Userbot berjalan...")
    app.run()
