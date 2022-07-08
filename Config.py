import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Zaid2_Robot")
    SUPPORT = os.environ.get("SUPPORT", "kk_kovilakam")
    CHANNEL = os.environ.get("CHANNEL", "KANTHARI_WRITINGS")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/1aaf04b524b231ae0d7b1.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/1aaf04b524b231ae0d7b1.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6435225"))
