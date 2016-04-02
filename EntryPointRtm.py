import time
from slackclient import SlackClient
from slacker import Slacker
from TeamcityUtils import get_project_names

token = ""

slack = Slacker(token)

commands = {"bot": 'Somebody call me?',
            "bot commands": "Im currently useless and can do nothing,"
                            " hope soon i will learn some cool stuff",
            "bot projects": get_project_names()}


def process_message(api, message):
    if "text" in message:
        message_content = message["text"]

        if message_content in commands:
            api.chat.post_message("#hackaton-bot", commands[message_content], 'bombila')

sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        message = sc.rtm_read()
        if len(message) != 0:
            unpacked = message[0]
            process_message(slack, unpacked)

        time.sleep(1)
else:
    print("Connection Failed, invalid token?")




