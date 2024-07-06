import os


class Config(object):
    API_HASH = os.environ.get("a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.environ.get("")
    TELEGRAM_API = os.environ.get("21740783")
    OWNER = os.environ.get("6299192020")
    OWNER_USERNAME = os.environ.get("speedwolf1")
    PASSWORD = os.environ.get("Anime_Warrior")
    DATABASE_URL = os.environ.get("mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
    LOGCHANNEL = os.environ.get("-1002040299414")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
