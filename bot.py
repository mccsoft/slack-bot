from slacker import Slacker

from commands import commands
from config_provider import config_provider
from message_generator import MessageGenerator
from сommand_worker import parse_command


class ProcessMessageHandler:

    def __init__(self):
        pass

    def is_alive(self):
        return True

    def handle(self, message, generator):
        message_content = message.text
        parse_command(message_content)
        if message_content in commands:
            commands[message_content]()


class Bot:

    def __init__(self):
        self.token = config_provider.token
        self.bot_name, self.channel_name = config_provider.bot_settings()
        self.slack = Slacker(self.token)



    def run(self):
        self.generator = MessageGenerator(self.token)
        self.generator.add_handler(ProcessMessageHandler())
        self.generator.run()
