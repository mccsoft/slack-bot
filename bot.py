import time
from slackclient import SlackClient
from slacker import Slacker
from commands import commands
from config_provider import config_provider
from slack_utils import get_channel_id
from сommand_worker import parse_command


class Bot:

    def __init__(self):
        self.token = config_provider.token
        self.bot_name, self.channel_name = config_provider.bot_settings()
        self.slack = Slacker(self.token)


    def process_message(self, api, message):
        if "text" in message:
            message_content = message["text"]
            parse_command(message_content)
            if message_content in commands:
                commands[message_content]()

    def run(self):
        sc = SlackClient(self.token)

        if sc.rtm_connect():
            while True:
                message = sc.rtm_read()
                if len(message) != 0:
                    print(message)
                    if "channel" in message[0]:
                        if message[0]["channel"] == get_channel_id(self.channel_name[1:]):
                            unpacked = message[0]
                            print(unpacked)
                            self.process_message(self.slack, unpacked)

                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")
