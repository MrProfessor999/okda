# Modified by NAVIN

import os
from os import getenv
import telegram.ext as tg

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EDIT_REPO")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
USERNAME = getenv("USERNAME")
NAME = getenv("NAME")
GENIUS = "false"
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MUSIC_PLAYER")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "EDIT_REPO")
PROJECT_NAME = getenv("PROJECT_NAME", "MUSIC_PLAYER v4")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Navipavi6818/MUSIC_PLAYER_BOT-V4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
TMDBAPI = getenv("TMDBAPI", None)
