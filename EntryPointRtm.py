import time
from slackclient import SlackClient
from slacker import Slacker

token = "xoxp-3112620471-7040594676-31516333026-b4642a3eef"

slack = Slacker(token)

commands = {"bot": 'Somebody call me?',
            "bot commands": "Im currently useless and can do nothing,"
                            " hope soon i will learn some cool stuff"}


def process_message(api, message):
    if "text" in message:
        message_content = message["text"]

        if message_content in commands:
            api.chat.post_message("#hackaton-bot", commands[message_content])

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




