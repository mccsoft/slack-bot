import time
import json
from slackclient import SlackClient
from slacker import Slacker
from сommand_worker import parse_command
from commands import commands
from collections import namedtuple

with open('appsettings.json') as config_file:
    config = json.load(config_file, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

token = config.token
bot_settings = config.bot_settings

channel_name = bot_settings.channel_name

slack = Slacker(token)

channel_id = ""

for channel in slack.channels.list().body['channels']:
    if channel['name'] == channel_name[1:]:
        channel_id = channel['id']

print(channel_id)

def process_message(api, message):
    if "text" in message:
        message_content = message["text"]
        parse_command(message_content)
        if message_content in commands:
            api.chat.post_message(bot_settings.channel_name, commands[message_content], bot_settings.bot_name)

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




