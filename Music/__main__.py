import requests
from pyrogram import Client as bot
from pyrogram import Client
from Music.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from Music import config

bot = bot(config.API_ID, config.API_HASH)
run = bot.run
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Music.modules"),
)

bot.start()
run()
