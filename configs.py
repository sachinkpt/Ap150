from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19099900"))
    API_HASH = getenv("API_HASH", "2b445de78e5baf012a0793e60bd4fbf5")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "illuminatiXNetwork")
    CHID = int(getenv("CHID", "-1002115636462"))
    SUDO = list(map(int, getenv("SUDO", "6299128233").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
