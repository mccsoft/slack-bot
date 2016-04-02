import time
from slackclient import SlackClient
from slacker import Slacker
from TeamcityUtils import get_project_names
from Config import token


slack = Slacker(token)

commands = {"bot": 'Somebody call me?',
            "bot commands": "Im currently useless and can do nothing,"
                            " hope soon i will learn some cool stuff",
            "bot projects": get_project_names()}

real_commands = {"build" : ""}
parameters = {"branch"}


def execute_command(function, parameter):
    pass


def parse_command(api, message_content):
    print(message_content[0])
    if message_content[0] == "!":
        array_of_words = message_content[1:].split()
        if array_of_words[0] in real_commands:
            if array_of_words[1] in parameters:
                execute_command(array_of_words[0], array_of_words[1])


def process_message(api, message):
    if "text" in message:
        message_content = message["text"]
        parse_command(api, message_content)
        if message_content in commands:
            api.chat.post_message("#hackaton-bot", commands[message_content], 'bombila')



sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        message = sc.rtm_read()
        if len(message) != 0:
            print(message[0])
            if "channel" in message[0]:
                if message[0]["channel"] == "C0XF2E0RY":
                    unpacked = message[0]
                    print(unpacked)
                    process_message(slack, unpacked)

        time.sleep(1)
else:
    print("Connection Failed, invalid token?")




