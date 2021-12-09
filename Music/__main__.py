import requests
from pyrogram import Client as Bot

from Music.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from plugins import run

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Music.modules"),
)

bot.start()
run()
