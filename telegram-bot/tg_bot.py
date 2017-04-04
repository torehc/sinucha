#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
sys.path.append('../web/sinucha/')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sinucha.settings")
import django
django.setup()
from sinucha.settings_local import TOKEN_BOT
from control.models import User_Data

# Enable logging
"""
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
"""

def start(bot, update):
    update.message.reply_text('Hi!')
    user = update.message.from_user
    print(user.first_name)
    print(user.username)
    print(user.id)


def help(bot, update):
    update.message.reply_text('Help!')


def echo(bot, update):
    update.message.reply_text(update.message.text)
    
def saldo(bot, update):
    tg_user = update.message.from_user #Telegram User
    #import pdb; pdb.set_trace()
    user = User_Data.objects.get(chatid=tg_user.id)
    update.message.reply_text('Su saldo es: '+str(user.balance_actual)+'€')

def registro(bot, update):
    tg_user = update.message.from_user #Telegram User
    


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN_BOT)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("saldo", saldo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()