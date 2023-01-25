from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 7009965)
API_HASH = config("API_HASH", "06651b174c4f0591deb0ed1e5663c996")
BOT_TOKEN = config("BOT_TOKEN", "5853309411:AAEP8YE6_vTsqb30PRtidv45Rww0GKCwxdo")
BOT_UN = config("BOT_UN", "prasadx_test_Bot")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
