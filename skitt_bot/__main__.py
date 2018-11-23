import telegram
import importlib
from skitt_bot.modules import ALL_MODULES
from skitt_bot import dispatcher, logger, updater, TOKEN, WEBHOOK, LISTEN, CERT_PATH, PORT, URL, logger
from telegram import Update, Bot
from telegram.ext import CommandHandler, run_async

IMPORTED = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("skitt_bot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

START_TEXT = """
Hey fam! I'm {}, and I'm here to bring some funny maymays into your life!
Check out /help for a full list of my commands with detailed descriptions.
""".format(dispatcher.bot.first_name)

HELP_TEXT = """
Ohai, I see you'd like to know what memes I have for sale.
Well, here you go.

Commands:
 <reply> = replying to a message
 <args> = adding a message after the command
 - /🅱 - <reply> - replying to a message with replace a random character with the B emoji.
 - /👏 - <reply> - adds clap emojis at the begining, end, and in every space in a message.
 - /😂 - <reply> - a replica of mattatas copypasta command.
 - /deepfry - <reply> - for when your images/stickers need to get a little fried.
 - /dllm - <optional args> - sends a random chinese meme. if you add a number after the command, itll reply with a specific photo.
 - /forbes - <reply> - turns a message into a Forbes headline.
 - me too - Saying "me too" will have a small chance for the bot to make a remark.
 - /mock - <reply> - mocks a replied message lick the spongebob meme.
 - /owo - <reply> - OwO whats this? OwOfies a message.
 - /stretch - <reply> - stretches vowels in a message a random number of times.
 - /thonkify - <reply>/<args> - turns text into thonk text (only supports letters and none symbols for now).
 - /vapor - <reply>/<args> - turns a message into vaporwave text.
 - /zalgofy - <reply> - corrupts a message.
"""

@run_async
def start(bot: Bot, update: Update):
    if update.effective_chat.type == "private":
        update.effective_message.reply_text(START_TEXT)
    else:
        update.effective_message.reply_text("Waow sur, you've UwU-ken me :3")

@run_async
def help(bot: Bot, update: Update):
    if update.effective_chat.type == "private":
        update.effective_message.reply_text(HELP_TEXT)
    else:
        update.effective_message.reply_text("Try this command again in a private message.")

def main():
    START_HANDLER = CommandHandler("start", start)
    HELP_HANDLER = CommandHandler("help", help)

    dispatcher.add_handler(START_HANDLER)
    dispatcher.add_handler(HELP_HANDLER)

    if WEBHOOK:
        logger.info("Using webhooks.")
        updater.start_webhook(listen=LISTEN,
                              port=PORT,
                              url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN,
                                    certificate=open(CERT_PATH, 'rb'))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        logger.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4)

    updater.idle()

if __name__ == '__main__':
    logger.info("Successfully loaded modules: " + str(ALL_MODULES))
    main()