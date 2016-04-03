from slackclient import SlackClient
import threading
from slack_utils import get_user_by_id
from slack_utils import get_channel_by_id
from config_provider import config_provider

#TODO try to rework with async await

bot_name, channel_name = config_provider.bot_settings()


class MessageWrapper:

    def __init__(self, json_message):
        self.__dict__ = json_message

    def channel_name(self):
        return get_channel_by_id(self.channel)

    def user_name(self):
        return get_user_by_id(self.user)


class MessageGenerator:

    def __init__(self, token):
        self.slack_client = SlackClient(token)
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def run(self):
        threading.Thread(target=self.start).start()

    def start(self):
        if self.slack_client.rtm_connect():
            while True:
                message = self.slack_client.rtm_read()

                if len(message):
                    wrapped_message = MessageWrapper(message[0])

                    if wrapped_message.type == "message":
                        if wrapped_message.channel_name() == channel_name[1:]:
                            for handler in self.handlers:
                                if handler.is_alive():
                                    handler.handle(wrapped_message, self)
                                else:
                                    self.handlers.remove(handler)



