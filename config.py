import logging
import os

BACKEND = "Mattermost"

BOT_DATA_DIR = r"/bot/data"
BOT_EXTRA_PLUGIN_DIR = r"/bot/plugins"
BOT_EXTRA_BACKEND_DIR = "/usr/local/lib/python3.10/site-packages"

BOT_LOG_FILE = r"/bot/errbot.log"
BOT_LOG_LEVEL = logging.INFO

BOT_ADMINS = (
    "@CHANGE_ME",
)  # Don't leave this as "@CHANGE_ME" if you connect your errbot to a chat system!!

BOT_IDENTITY = {
    # Required
    "team": "nameoftheteam",
    "server": "mattermost.server.com",
    "token": "YourPersonalAccessToken",
    "insecure": False,                  # Default = False. Set to true for self signed certificates
    "scheme": "https",                  # Default = https
    "port": 443,                       # Default = 8065
    "timeout": 30                      # Default = 30. If the webserver disconnects idle connections later/earlier change this value
    #"cards_hook": "incomingWebhookId"   # Needed for cards/attachments
}
