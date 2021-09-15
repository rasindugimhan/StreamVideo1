from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", None)
API_ID = int(getenv("API_ID", "6"))
API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION_NAME = getenv("SESSION_NAME", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "dihanofficial")
BOT_USERNAME = getenv("BOT_USERNAME", "TheNatsukiBot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
SESSION_STRING = getenv("SESSION_NAME", "")
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
