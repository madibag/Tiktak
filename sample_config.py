import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    #jsonpath
    Dowloadloc = "./JSON"

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
