from pyrogram import Client
from os import listdir

from Music import config
from Music.services.converter import convert
from Music.services.downloaders import youtube
from Music.services.queues import queues


if "raw_files" not in listdir():
    mkdir("raw_files")

__all__ = ["convert"]

__all__ = ["youtube"]

__all__ = ["clear", "get", "is_empty", "put", "task_done"]


client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
