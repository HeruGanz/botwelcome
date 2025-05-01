import logging
from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Client(
    name="userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    plugins={"root": "plugins"}
)

logger.info("🟢 Memulai userbot...")
app.run()
