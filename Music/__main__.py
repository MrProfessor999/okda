import requests
from pyrogram import Client as Bot

from Music.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN , BANNER, LOG
from plugins import run

response = requests.get(BG_IMAGE)
file = open("./plugins/foreground.png", "wb")
file.write(response.content)
file.close()
 
LOG.info("%s", BANNER)

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Music.modules"),
)

bot.start()
run()
