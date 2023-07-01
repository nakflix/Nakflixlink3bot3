# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6144375431:AAE48FZtzomh9pf-5D4kbrQROp7hdOp9lB4")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14298205"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "28df6d84da76d8606bf5f0e71ecfb62c")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001755253960"))

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "netflixxebot")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "d188bce9-be3d-42f5-8b14-222d5cfb90d1")

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kidderke8:alpha3720@netflixxe.tixwcbz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "netflixxe")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001858872654"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001861505272"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001585995212"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>ʜᴇʟʟᴏ {first}</b>\n\n<b>ɪ ᴄᴀɴ sᴀᴠᴇ ᴀ ᴘᴇʀsᴏɴᴀʟ ғɪʟᴇ ᴏɴ @NAKFLIXTV ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋs.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1458235021").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>ʜᴇʟʟᴏ {first}\n\nʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘ ғɪʀsᴛ ᴛᴏ sᴇᴇ ᴛʜᴇ ʜɪᴅᴅᴇɴ ғɪʟᴇ\n\nᴋɪɴᴅʟʏ 👇ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘ ғɪʀsᴛ👇</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "ᴊᴏɪɴ @NAKFLIXTV")

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
