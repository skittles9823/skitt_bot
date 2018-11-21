import logging
from os import path
import telegram.ext

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

if path.exists("skitt_bot/config.py"):
    from skitt_bot.config import Config
    TOKEN = Config.API_KEY
    DEEPFRY_TOKEN = Config.DEEPFRY_TOKEN
else:
    logger.error("config.py not found! Quitting.")
    exit(-1)

updater = telegram.ext.Updater(TOKEN)
dispatcher = updater.dispatcher