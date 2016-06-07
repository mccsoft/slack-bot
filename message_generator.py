from slacksocket import SlackSocket
import threading
import pykka
from config_provider import config_provider
import json


bot_name, channel_name = config_provider.bot_settings()


class MessageWrapper:

    def __init__(self, json_message):
        self.__dict__ = json_message

    def channel_name(self):
        if hasattr(self, "channel"):
            return self.channel

    def user_name(self):
        if hasattr(self, "user"):
            return self.user


class MessageGenerator:

    def run(self):
        threading.Thread(target=self.start).start()

    def start(self):
        socket = SlackSocket(config_provider.token, translate=True)

        for event in socket.events():
            message = MessageWrapper(json.loads(event.json))

            if message.type == "message":
                pykka.ActorRegistry.broadcast(message.__dict__)
