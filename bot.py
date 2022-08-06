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
        sendMessageOwner("📝 New issue opened\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'closed':
        # If the issue is closed, send a message to the owner id
        sendMessageOwner("📝 Issue closed\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'reopened':
        # If the issue is reopened, send a message to the owner id
        sendMessageOwner("📝 Issue reopened\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'labeled':
        # If the issue is labeled, send a message to the owner id
        sendMessageOwner("📝 Issue labeled\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'unlabeled':
        # If the issue is unlabeled, send a message to the owner id
        sendMessageOwner("📝 Issue unlabeled\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'assigned':
        # If the issue is assigned, send a message to the owner id
        sendMessageOwner("📝 Issue assigned\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'unassigned':
        # If the issue is unassigned, send a message to the owner id
        sendMessageOwner("📝 Issue unassigned\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'synchronize':
        # If the issue is synchronized, send a message to the owner id
        sendMessageOwner("📝 Issue synchronized\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_requested':
        # If the issue is review requested, send a message to the owner id
        sendMessageOwner("📝 Review requested\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_removed':
        # If the issue is review request removed, send a message to the owner id
        sendMessageOwner("📝 Review request removed\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_approved':
        # If the issue is review request approved, send a message to the owner id
        sendMessageOwner("📝 Review request approved\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_changes_requested':
        # If the issue is review request changes requested, send a message to the owner id
        sendMessageOwner("📝 Review request changes requested\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_changes_approved':
        # If the issue is review request changes approved, send a message to the owner id
        sendMessageOwner("📝 Review request changes approved\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_changes_rejected':
        # If the issue is review request changes rejected, send a message to the owner id
        sendMessageOwner("📝 Review request changes rejected\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_dismissed':
        # If the issue is review request dismissed, send a message to the owner id
        sendMessageOwner("📝 Review request dismissed\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_removed':
        # If the issue is review request removed, send a message to the owner id
        sendMessageOwner("📝 Review request removed\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))
    elif data['action'] == 'review_request_commented':
        # If the issue is review request commented, send a message to the owner id
        sendMessageOwner("📝 Review request commented\n\nIssue title: %s\n\nLink: %s" % (data['issue']['title'], data['issue']['html_url']))

    # On commit
    elif data['action'] == 'committed':
        # If the commit is made, send a message to the owner id
        sendMessageOwner("📝 Commit made\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'created':
        # If the commit is created, send a message to the owner id
        sendMessageOwner("📝 Commit created\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'deleted':
        # If the commit is deleted, send a message to the owner id
        sendMessageOwner("📝 Commit deleted\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'restored':
        # If the commit is restored, send a message to the owner id
        sendMessageOwner("📝 Commit restored\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'referenced':
        # If the commit is referenced, send a message to the owner id
        sendMessageOwner("📝 Commit referenced\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'unreferenced':
        # If the commit is unreferenced, send a message to the owner id
        sendMessageOwner("📝 Commit unreferenced\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'renamed':
        # If the commit is renamed, send a message to the owner id
        sendMessageOwner("📝 Commit renamed\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'edited':
        # If the commit is edited, send a message to the owner id
        sendMessageOwner("📝 Commit edited\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'commented':
        # If the commit is commented, send a message to the owner id
        sendMessageOwner("📝 Commit commented\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'labeled':
        # If the commit is labeled, send a message to the owner id
        sendMessageOwner("📝 Commit labeled\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'unlabeled':
        # If the commit is unlabeled, send a message to the owner id
        sendMessageOwner("📝 Commit unlabeled\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'milestoned':
        # If the commit is milestoned, send a message to the owner id
        sendMessageOwner("📝 Commit milestoned\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'demilestoned':
        # If the commit is demilestoned, send a message to the owner id
        sendMessageOwner("📝 Commit demilestoned\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'pinned':
        # If the commit is pinned, send a message to the owner id
        sendMessageOwner("📝 Commit pinned\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'unpinned':
        # If the commit is unpinned, send a message to the owner id
        sendMessageOwner("📝 Commit unpinned\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'locked':
        # If the commit is locked, send a message to the owner id
        sendMessageOwner("📝 Commit locked\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'unlocked':
        # If the commit is unlocked, send a message to the owner id
        sendMessageOwner("📝 Commit unlocked\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'review_requested':
        # If the commit is review requested, send a message to the owner id
        sendMessageOwner("📝 Commit review requested\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))
    elif data['action'] == 'review_request_removed':
        # If the commit is review request removed, send a message to the owner id
        sendMessageOwner("📝 Commit review request removed\n\nCommit message: %s\n\nLink: %s" % (data['commit']['message'], data['commit']['url']))     
    

    # If the action is not one of the above, send a message to the owner id
    else:   
        sendMessageOwner("📝 Issue action: %s" % data['action'])

    return Response("OK", status=200)

@app.route('/', methods=['GET'])
@limiter.limit("5/minute") 
def home():
    return Response("Welcome")
    
app.run(port=3000)