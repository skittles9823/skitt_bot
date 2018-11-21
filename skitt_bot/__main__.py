import telegram
import importlib
from skitt_bot.modules import ALL_MODULES
from skitt_bot import updater

IMPORTED = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("skitt_bot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

updater.start_polling(timeout=15, read_latency=4)
updater.idle()