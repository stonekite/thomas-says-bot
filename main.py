from telegram.ext import Updater, MessageHandler
from handlers import message_handler
import logging
from keys import bot_token



def main():
    logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)
    updater = Updater(bot_token)
    updater.dispatcher.add_handler(MessageHandler(filters=None, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
