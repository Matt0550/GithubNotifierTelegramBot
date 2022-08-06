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
    data = request.get_data()
    data = json.loads(data)
    print(data)
    print(data.get('action'))
    # ISSUE
    if data.get('action') == 'opened' and data.get("issue") is not None:
        # If the issue is opened, send a message to the owner id
        sendMessageOwner("📝 New issue opened:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'closed' and data.get("issue") is not None:
        # If the issue is closed, send a message to the owner id
        sendMessageOwner("📝 Issue closed:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'deleted' and data.get("issue") is not None:
        # If the issue is deleted, send a message to the owner id
        sendMessageOwner("📝 Issue deleted:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'assigned' and data.get("issue") is not None:
        # If the issue is assigned, send a message to the owner id
        sendMessageOwner("📝 Issue assigned:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'unassigned' and data.get("issue") is not None:
        # If the issue is unassigned, send a message to the owner id
        sendMessageOwner("📝 Issue unassigned:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'labeled' and data.get("issue") is not None:
        # If the issue is labeled, send a message to the owner id
        sendMessageOwner("📝 Issue labeled:\nIssue title: %s\nIssue url: %s\nLabel: %s" % (data["issue"]["title"], data["issue"]["html_url"], data["label"]["name"]))
    elif data.get('action') == 'unlabeled' and data.get("issue") is not None:
        # If the issue is unlabeled, send a message to the owner id
        sendMessageOwner("📝 Issue unlabeled:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'synchronize' and data.get("issue") is not None:
        # If the issue is synchronized, send a message to the owner id
        sendMessageOwner("📝 Issue synchronized:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'reopened' and data.get("issue") is not None:
        # If the issue is reopened, send a message to the owner id
        sendMessageOwner("📝 Issue reopened:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'review_requested' and data.get("issue") is not None:
        # If the issue is review requested, send a message to the owner id
        sendMessageOwner("📝 Issue review requested:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'review_request_removed' and data.get("issue") is not None:
        # If the issue is review request removed, send a message to the owner id
        sendMessageOwner("📝 Issue review request removed:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'locked' and data.get("issue") is not None:
        # If the issue is locked, send a message to the owner id
        sendMessageOwner("📝 Issue locked:\nIssue title: %s\nIssue url: %s\nLock reason: %s" % (data["issue"]["title"], data["issue"]["html_url"], data["lock_reason"]))
    elif data.get('action') == 'unlocked' and data.get("issue") is not None:
        # If the issue is unlocked, send a message to the owner id
        sendMessageOwner("📝 Issue unlocked:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'pinned' and data.get("issue") is not None:
        # If the issue is pinned, send a message to the owner id
        sendMessageOwner("📝 Issue pinned:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'unpinned' and data.get("issue") is not None:
        # If the issue is unpinned, send a message to the owner id
        sendMessageOwner("📝 Issue unpinned:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'edited' and data.get("issue") is not None:
        # If the issue is edited, send a message to the owner id
        sendMessageOwner("📝 Issue edited:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'milestoned' and data.get("issue") is not None:
        # If the issue is milestoned, send a message to the owner id
        sendMessageOwner("📝 Issue milestoned:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'demilestoned' and data.get("issue") is not None:
        # If the issue is demilestoned, send a message to the owner id
        sendMessageOwner("📝 Issue demilestoned:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    elif data.get('action') == 'transferred' and data.get("issue") is not None:
        # If the issue is transferred, send a message to the owner id
        sendMessageOwner("📝 Issue transferred:\nIssue title: %s\nIssue url: %s" % (data["issue"]["title"], data["issue"]["html_url"]))
    
    # MILESTONE
    elif data.get('action') == 'created' and data.get("milestone") is not None:
        # If the milestone is created, send a message to the owner id
        sendMessageOwner("📝 New milestone created:\nMilestone title: %s\nMilestone url: %s" % (data["milestone"]["title"], data["milestone"]["html_url"]))
    elif data.get('action') == 'closed' and data.get("milestone") is not None:
        # If the milestone is closed, send a message to the owner id
        sendMessageOwner("📝 Milestone closed:\nMilestone title: %s\nMilestone url: %s" % (data["milestone"]["title"], data["milestone"]["html_url"]))
    elif data.get('action') == 'deleted' and data.get("milestone") is not None:
        # If the milestone is deleted, send a message to the owner id
        sendMessageOwner("📝 Milestone deleted:\nMilestone title: %s\nMilestone url: %s" % (data["milestone"]["title"], data["milestone"]["html_url"]))
    elif data.get('action') == 'opened' and data.get("milestone") is not None:
        # If the milestone is opened, send a message to the owner id
        sendMessageOwner("📝 Milestone opened:\nMilestone title: %s\nMilestone url: %s" % (data["milestone"]["title"], data["milestone"]["html_url"]))
    elif data.get('action') == 'reopened' and data.get("milestone") is not None:
        # If the milestone is reopened, send a message to the owner id
        sendMessageOwner("📝 Milestone reopened:\nMilestone title: %s\nMilestone url: %s" % (data["milestone"]["title"], data["milestone"]["html_url"]))
    elif data.get('action') == 'edited' and data.get("milestone") is not None:
        # If the milestone is edited, send a message to the owner id
        sendMessageOwner("📝 Milestone edited:\nMilestone title: %s\nMilestone url: %s" % (data["milestone"]["title"], data["milestone"]["html_url"]))
        
    # PULL REQUEST
    elif data.get('action') == 'opened' and data.get("pull_request") is not None:
        # If the pull request is opened, send a message to the owner id
        sendMessageOwner("📝 New pull request opened:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'closed' and data.get("pull_request") is not None:
        # If the pull request is closed, send a message to the owner id
        sendMessageOwner("📝 Pull request closed:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'reopened' and data.get("pull_request") is not None:
        # If the pull request is reopened, send a message to the owner id
        sendMessageOwner("📝 Pull request reopened:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'edited' and data.get("pull_request") is not None:
        # If the pull request is edited, send a message to the owner id
        sendMessageOwner("📝 Pull request edited:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'assigned' and data.get("pull_request") is not None:
        # If the pull request is assigned, send a message to the owner id
        sendMessageOwner("📝 Pull request assigned:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'unassigned' and data.get("pull_request") is not None:
        # If the pull request is unassigned, send a message to the owner id
        sendMessageOwner("📝 Pull request unassigned:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'review_requested' and data.get("pull_request") is not None:
        # If the pull request is review requested, send a message to the owner id
        sendMessageOwner("📝 Pull request review requested:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'review_request_removed' and data.get("pull_request") is not None:
        # If the pull request is review request removed, send a message to the owner id
        sendMessageOwner("📝 Pull request review request removed:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'labeled' and data.get("pull_request") is not None:
        # If the pull request is labeled, send a message to the owner id
        sendMessageOwner("📝 Pull request labeled:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'unlabeled' and data.get("pull_request") is not None:
        # If the pull request is unlabeled, send a message to the owner id
        sendMessageOwner("📝 Pull request unlabeled:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'synchronize' and data.get("pull_request") is not None:
        # If the pull request is synchronized, send a message to the owner id
        sendMessageOwner("📝 Pull request synchronized:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'ready_for_review' and data.get("pull_request") is not None:
        # If the pull request is ready for review, send a message to the owner id
        sendMessageOwner("📝 Pull request ready for review:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'locked' and data.get("pull_request") is not None:
        # If the pull request is locked, send a message to the owner id
        sendMessageOwner("📝 Pull request locked:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'unlocked' and data.get("pull_request") is not None:
        # If the pull request is unlocked, send a message to the owner id
        sendMessageOwner("📝 Pull request unlocked:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'milestoned' and data.get("pull_request") is not None:
        # If the pull request is milestoned, send a message to the owner id
        sendMessageOwner("📝 Pull request milestoned:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))
    elif data.get('action') == 'demilestoned' and data.get("pull_request") is not None:
        # If the pull request is demilestoned, send a message to the owner id
        sendMessageOwner("📝 Pull request demilestoned:\nPull request title: %s\nPull request url: %s" % (data["pull_request"]["title"], data["pull_request"]["html_url"]))

    # STAR
    elif data.get('action') == 'created' or data.get('action') == 'started' and data.get("starred_at") is not None:
        # If the repository is starred, send a message to the owner id
        sendMessageOwner("💚 New repository starred:\nRepository name: %s\nRepository url: %s" % (data["repository"]["name"], data["repository"]["html_url"]))
    elif data.get('action') == 'deleted' and data.get("starred_at") != "":
        # If the repository is unstarred, send a message to the owner id
        sendMessageOwner("💚 Repository unstarred:\nRepository name: %s\nRepository url: %s" % (data["repository"]["name"], data["repository"]["html_url"]))

    # COMMIT
    elif data.get('commits') is not None:
        # If the repository is pushed, send a message to the owner id
        sendMessageOwner("📝 New commit pushed:\nCommit message: %s\nCommitter: %s\nCommit url: %s" % (data["commits"][0]["message"], data["commits"][0]["committer"]["name"], data["commits"][0]["url"]))
    elif data.get('action') == 'created' and data.get("ref") is not None:
        # If the repository is created, send a message to the owner id
        sendMessageOwner("📝 New repository created:\nRepository name: %s\nRepository url: %s" % (data["repository"]["name"], data["repository"]["html_url"]))
    elif data.get('action') == 'deleted' and data.get("ref") is not None:
        # If the repository is deleted, send a message to the owner id
        sendMessageOwner("📝 Repository deleted:\nRepository name: %s\nRepository url: %s" % (data["repository"]["name"], data["repository"]["html_url"]))
    elif data.get('action') == 'edited' and data.get("ref") is not None:
        # If the repository is edited, send a message to the owner id
        sendMessageOwner("📝 Repository edited:\nRepository name: %s\nRepository url: %s" % (data["repository"]["name"], data["repository"]["html_url"]))

    else:
        sendMessageOwner("📝 Action: %s\nRepository name: %s\nRepository url: %s" % (data["action"], data["repository"]["name"], data["repository"]["html_url"]))

    return Response("OK", status=200)

@app.route('/', methods=['GET'])
@limiter.limit("5/minute") 
def home():
    return Response("Welcome")
    
app.run(port=3000)