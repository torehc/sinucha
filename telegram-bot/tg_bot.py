#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

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
    """
    print(user.first_name)
    print(user.username)
    print(user.id)
    """

def help(bot, update):
    update.message.reply_text('Help!')

def echo(bot, update):
    update.message.reply_text(update.message.text)
    
def saldo(bot, update):
    tg_user = update.message.from_user #Telegram User
    user = User_Data.objects.get(chatid=tg_user.id)
    update.message.reply_text('Su saldo es: '+str(user.balance_actual)+'€')

def registro(bot, update):
    
    tg_user = update.message.from_user #Telegram User
    
    if(User_Data.check_user_chatid(tg_user.id)):
        update.message.reply_text('Ya se ha registrado en el sistema')
    else:
        #Registar usuario
        update.message.reply_text('Bienvenido al Sistema de Registro')
        update.message.reply_text('Pase su tag RFID por el lector...')
        #¿Ha pasado el tag por el lector? Si/No
        keyboard = [[InlineKeyboardButton("SI", callback_data='SI')],

                [InlineKeyboardButton("NO", callback_data='SI')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('¿Ha pasado el tag por el lector?:', reply_markup=reply_markup)

def button(bot, update):
    query = update.callback_query
    
    bot.editMessageText(text="Elegido: %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
   
    if(query.data == 'SI'):
        infile = open('/var/run/last_rfid.tag', 'r')
        tag = infile.readline()
        infile.close()
        
        if( User_Data.register_user(query.message.chat_id, tag[:-1]) ):
            bot.editMessageText(text="Usuario creado correctamente",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
        else:
            bot.editMessageText(text="Usuario NO creado",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
    else:
        bot.editMessageText(text="Proceso Cancelado",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
                     
        

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN_BOT)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("saldo", saldo))
    dp.add_handler(CommandHandler("registro", registro))
    dp.add_handler(CallbackQueryHandler(button))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()