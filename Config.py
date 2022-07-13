import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "14071925"))
    API_HASH = os.environ.get("API_HASH", "5f14a90b6f505e80e8e25f061ad51e42")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5567453202:AAGUBvDK8pKmB3zxks3ZZOIdx8rbG229ufw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", "ENABLE")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "ENABLE")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Stenzle_MariaMusicbot")
    SUPPORT = os.environ.get("SUPPORT", "kk_kovilakam")
    CHANNEL = os.environ.get("CHANNEL", "KANTHARI_WRITINGS")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/1ec66485a71a68fe15392.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/1aaf04b524b231ae0d7b1.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5562423241"))
