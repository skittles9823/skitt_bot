import telegram
import importlib
from skitt_bot.modules import ALL_MODULES
from skitt_bot import updater, WEBHOOK, LISTEN, CERT_PATH, PORT, URL

IMPORTED = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("skitt_bot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

if WEBHOOK:
    LOGGER.info("Using webhooks.")
    updater.start_webhook(listen=LISTEN,
                          port=PORT,
                          url_path=TOKEN)

    if CERT_PATH:
        updater.bot.set_webhook(url=URL + TOKEN,
                                certificate=open(CERT_PATH, 'rb'))
    else:
        updater.bot.set_webhook(url=URL + TOKEN)

else:
    LOGGER.info("Using long polling.")
    updater.start_polling(timeout=15, read_latency=4)

updater.idle()