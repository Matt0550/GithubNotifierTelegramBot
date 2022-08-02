#################################
#   Tag Everyone Telegram Bot   #
# Developed by @Non_Sono_Matteo #
#       https://matt05.ml       #
#       Github: @Matt0550       #
#################################

import datetime
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json

import os
# from keep_alive import keep_alive # Replit hosting

OWNER_ID = 313344916

TOKEN = "5440019738:AAF4S4aVe1BZ-KnW_MuL687NJlSqzjUw-r8" # OR os.environ['token']

app = Flask(__name__)

updater = Updater(TOKEN, use_context=True)

limiter = Limiter(app, key_func=get_remote_address)

start_time = datetime.datetime.now() # For the uptime command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Github Notifier Bot!\n\nThis bot is developed by @Non_sono_Matteo\n\nYou can find the source code on github:\nhttps://github.com/Matt0550/GithubNotifierTelegramBot")

def status(update: Update, context: CallbackContext):
    # Get the bot uptime widout microseconds
    uptime = datetime.datetime.now() - start_time
    uptime = str(uptime).split(".")[0]

    update.message.reply_text("✅ If you see this message, the bot is working\n⏰ Uptime: %s" % str(uptime))

def sendMessageOwner(message):
    # Send message to owner id
    updater.bot.send_message(OWNER_ID, message)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('status', status))

# keep_alive() # Replit hosting
updater.start_polling()

# On bot start, send message to owner id
sendMessageOwner("✅ Bot started and ready to use") # Comment this line if you don't want to send a message to the owner when the bot starts

@app.route('/webhook', methods=['POST'])
@limiter.limit("5/minute") 
def respond():
    print(request.json)
    return Response(status=200)

@app.route('/', methods=['GET'])
@limiter.limit("5/minute") 
def home():
    return Response("Welcome")
    
app.run()