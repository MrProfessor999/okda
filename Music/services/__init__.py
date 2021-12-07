from pyrogram import Client
from os import listdir

from Music import config
from Music.services import converter
from Music.services import youtube
from Music.services import queues


client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
