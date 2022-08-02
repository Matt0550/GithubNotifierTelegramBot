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
from flask import Flask, Request, request, Response
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
def webhook():
    data = request.get_json()
    print(data)
    if data['action'] == 'opened':
        # If the issue is opened, send a message to the owner id
        sendMessageOwner("📝 New issue opened: %s" % data['issue']['title'])
    elif data['action'] == 'closed':
        # If the issue is closed, send a message to the owner id
        sendMessageOwner("📝 Issue closed: %s" % data['issue']['title'])
    elif data['action'] == 'reopened':
        # If the issue is reopened, send a message to the owner id
        sendMessageOwner("📝 Issue reopened: %s" % data['issue']['title'])
    elif data['action'] == 'labeled':
        # If the issue is labeled, send a message to the owner id
        sendMessageOwner("📝 Issue labeled: %s" % data['issue']['title'])
    elif data['action'] == 'unlabeled':
        # If the issue is unlabeled, send a message to the owner id
        sendMessageOwner("📝 Issue unlabeled: %s" % data['issue']['title'])
    elif data['action'] == 'assigned':
        # If the issue is assigned, send a message to the owner id
        sendMessageOwner("📝 Issue assigned: %s" % data['issue']['title'])
    elif data['action'] == 'unassigned':
        # If the issue is unassigned, send a message to the owner id
        sendMessageOwner("📝 Issue unassigned: %s" % data['issue']['title'])
    elif data['action'] == 'reopened':
        # If the issue is reopened, send a message to the owner id
        sendMessageOwner("📝 Issue reopened: %s" % data['issue']['title'])
    elif data['action'] == 'synchronize':
        # If the issue is synchronized, send a message
        sendMessageOwner("📝 Issue synchronized: %s" % data['issue']['title'])
    elif data['action'] == 'edited':
        # If the issue is edited, send a message to the owner id
        sendMessageOwner("📝 Issue edited: %s" % data['issue']['title'])
    elif data['action'] == 'milestoned':
        # If the issue is milestoned, send a message to the owner id
        sendMessageOwner("📝 Issue milestoned: %s" % data['issue']['title'])
    elif data['action'] == 'demilestoned':
        # If the issue is demilestoned, send a message to the owner id
        sendMessageOwner("📝 Issue demilestoned: %s" % data['issue']['title'])
    elif data['action'] == 'renamed':
        # If the issue is renamed, send a message to the owner id
        sendMessageOwner("📝 Issue renamed: %s" % data['issue']['title'])
    elif data['action'] == 'locked':
        # If the issue is locked, send a message to the owner id
        sendMessageOwner("📝 Issue locked: %s" % data['issue']['title'])
    elif data['action'] == 'unlocked':
        # If the issue is unlocked, send a message to the owner id
        sendMessageOwner("📝 Issue unlocked: %s" % data['issue']['title'])
    elif data['action'] == 'review_requested':
        # If the issue is review requested, send a message to the owner id
        sendMessageOwner("📝 Issue review requested: %s" % data['issue']['title'])
    elif data['action'] == 'review_request_removed':
        # If the issue is review request removed, send a message to the owner id
        sendMessageOwner("📝 Issue review request removed: %s" % data['issue']['title'])
    elif data['action'] == 'review_requested_removed':
        # If the issue is review requested removed, send a message to the owner id
        sendMessageOwner("📝 Issue review requested removed: %s" % data['issue']['title'])
    elif data['action'] == 'review_completed':
        # If the issue is review completed, send a message to the owner id
        sendMessageOwner("📝 Issue review completed: %s" % data['issue']['title'])
    elif data['action'] == 'review_dismissed':
        # If the issue is review dismissed, send a message to the owner id
        sendMessageOwner("📝 Issue review dismissed: %s" % data['issue']['title'])
    elif data['action'] == 'review_dismissed_removed':
        # If the issue is review dismissed removed, send a message to the owner id
        sendMessageOwner("📝 Issue review dismissed removed: %s" % data['issue']['title'])
    elif data['action'] == 'review_completed_removed':
        # If the issue is review completed removed, send a message to the owner id
        sendMessageOwner("📝 Issue review completed removed: %s" % data['issue']['title'])
    elif data['action'] == 'review_comment':
        # If the issue is review comment, send a message to the owner id
        sendMessageOwner("📝 Issue review comment: %s" % data['issue']['title'])
    elif data['action'] == 'review_dismissed_comment':
        # If the issue is review dismissed comment, send a message to the owner id
        sendMessageOwner("📝 Issue review dismissed comment: %s" % data['issue']['title'])
    elif data['action'] == 'review_requested_comment':
        # If the issue is review requested comment, send a message to the owner id
        sendMessageOwner("📝 Issue review requested comment: %s" % data['issue']['title'])
    elif data['action'] == 'review_request_removed_comment':
        # If the issue is review request removed comment, send a message to the owner id
        sendMessageOwner("📝 Issue review request removed comment: %s" % data['issue']['title'])
    elif data['action'] == 'review_requested_removed_comment':
        # If the issue is review requested removed comment, send a message to the owner id
        sendMessageOwner("📝 Issue review requested removed comment: %s" % data['issue']['title'])
    elif data['action'] == 'review_completed_comment':
        # If the issue is review completed comment, send a message to the owner id
        sendMessageOwner("📝 Issue review completed comment: %s" % data['issue']['title'])
    elif data['action'] == 'review_completed_removed_comment':
        # If the issue is review completed removed comment, send a message to the owner id
        sendMessageOwner("📝 Issue review completed removed comment: %s" % data['issue']['title'])  
    elif data['action'] == 'review_dismissed_comment':
        # If the issue is review dismissed comment, send a message to the owner id
        sendMessageOwner("📝 Issue review dismissed comment: %s" % data['issue']['title'])

    # If the action is not one of the above, send a message to the owner id
    else:   
        sendMessageOwner("📝 Issue action: %s" % data['issue']['title'])

@app.route('/', methods=['GET'])
@limiter.limit("5/minute") 
def home():
    return Response("Welcome")
    
app.run(port=3000)