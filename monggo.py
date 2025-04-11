from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ChatMemberHandler, ContextTypes
from pymongo import MongoClient

# ========== Konfigurasi ==========

TOKEN = '7852362560:AAEn4kH47IMsvozYVP2HsA7R_hAfYo8KQiE'
MONGO_URI = 'mongodb+srv://heru07:admin1337@cluster0.blp8n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Koneksi MongoDB
client = MongoClient(MONGO_URI)
db = client['botDB']  # nama database
users_col = db['users']  # nama koleksi (table)

# ========== Handler ==========

# Handler untuk user yang join grup
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        user_data = {
            "user_id": member.id,
            "username": member.username,
            "first_name": member.first_name,
            "joined_group": update.chat_member.chat.title
        }
        users_col.update_one({"user_id": member.id}, {"$set": user_data}, upsert=True)
        
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=f"Halo {member.full_name}, selamat datang di grup! 🎉"
        )

# Handler untuk /start (chat pribadi)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    users_col.update_one(
        {"user_id": user.id},
        {"$set": {
            "user_id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "chat_type": "private"
        }},
        upsert=True
    )

    await update.message.reply_text(f"Halo {user.first_name}! Selamat datang! 🤖")

# ========== Main Bot ==========

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

    print("Bot aktif dan terhubung ke MongoDB...")
    app.run_polling()
