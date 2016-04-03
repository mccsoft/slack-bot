from config_provider import config_provider
from message_generator import MessageGenerator
from handlers.process_message_handler import ProcessMessageHandler


class Bot:

    def __init__(self):
        self.token = config_provider.token
        self.generator = MessageGenerator(self.token)

    def run(self):
        self.generator.add_handler(ProcessMessageHandler())
        self.generator.run()
