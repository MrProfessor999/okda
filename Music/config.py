# Modified by NAVIN

import os
from os import getenv
import telegram.ext as tg

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EDIT_REPO")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
BG_IMAGE = getenv("BG_IMAGE")
USERNAME = getenv("USERNAME")
NAME = getenv("NAME")
GENIUS = "false"
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MUSIC_PLAYER")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "EDIT_REPO")
PROJECT_NAME = getenv("PROJECT_NAME", "MUSIC_PLAYER v4")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Navipavi6818/MUSIC_PLAYER_BOT-V4")
TMDBAPI = getenv("TMDBAPI", None)



