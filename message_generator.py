from slackclient import SlackClient
import threading
import pykka
from slack_utils import get_user_by_id
from slack_utils import get_channel_by_id
from config_provider import config_provider


bot_name, channel_name = config_provider.bot_settings()


class MessageWrapper:

    def __init__(self, json_message):
        self.__dict__ = json_message

    def channel_name(self):
        if hasattr(self, "channel"):
            return get_channel_by_id(self.channel)

    def user_name(self):
        if hasattr(self, "user"):
            return get_user_by_id(self.user)


class MessageGenerator:

    def __init__(self, token):
        self.slack_client = SlackClient(token)

    def run(self):
        threading.Thread(target=self.start).start()

    def start(self):
        if self.slack_client.rtm_connect():
            while True:
                message = self.slack_client.rtm_read()
                if len(message):
                    wrapped_message = MessageWrapper(message[0])

                    if wrapped_message.type == "message":
                        pykka.ActorRegistry.broadcast(wrapped_message.__dict__)
