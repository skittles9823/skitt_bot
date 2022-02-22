import logging
import os
from os import path

import telegram.ext

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    LISTEN = os.environ.get('0.0.0.0', "")
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    DEEPFRY_TOKEN = os.environ.get('DEEPFRY_TOKEN', "")
elif path.exists("skitt_bot/config.py"):
    from skitt_bot.config import Config
    TOKEN = Config.API_KEY
    WEBHOOK = Config.WEBHOOK
    LISTEN = Config.LISTEN
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    DEEPFRY_TOKEN = Config.DEEPFRY_TOKEN


updater = telegram.ext.Updater(TOKEN)
dispatcher = updater.dispatcher
