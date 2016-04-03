import time

from slackclient import SlackClient
from slacker import Slacker

from commands import commands
from config_provider import config_provider
from slack_utils import get_channel_id
from сommand_worker import parse_command

token = config_provider.token

bot_name, channel_name = config_provider.bot_settings()

slack = Slacker(token)


def process_message(api, message):
    if "text" in message:
        message_content = message["text"]
        parse_command(message_content)
        if message_content in commands:
            api.chat.post_message(channel_name, commands[message_content], bot_name)


sc = SlackClient(token)

if sc.rtm_connect():
    while True:
        message = sc.rtm_read()
        if len(message) != 0:
            print(message)
            if "channel" in message[0]:
                if message[0]["channel"] == get_channel_id(channel_name[1:]):
                    unpacked = message[0]
                    print(unpacked)
                    process_message(slack, unpacked)

        time.sleep(1)
else:
    print("Connection Failed, invalid token?")
