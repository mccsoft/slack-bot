import time
from slackclient import SlackClient
from slacker import Slacker
from config import token
from сommand_worker import parse_command
from commands import commands

slack = Slacker(token)

def process_message(api, message):
    if "text" in message:
        message_content = message["text"]
        parse_command(message_content)
        if message_content in commands:
            api.chat.post_message("#hackaton-bot", commands[message_content], 'bombila')

sc = SlackClient(token)

if sc.rtm_connect():
    while True:
        message = sc.rtm_read()
        if len(message) != 0:
            if "channel" in message[0]:
                if message[0]["channel"] == "C0XF2E0RY":
                    unpacked = message[0]
                    print(unpacked)
                    process_message(slack, unpacked)

        time.sleep(1)
else:
    print("Connection Failed, invalid token?")




