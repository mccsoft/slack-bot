from сommand_worker import parse_command
from commands import commands


class ProcessMessageHandler:

    def __init__(self):
        self.alive = True

    def is_alive(self):
        return self.alive

    def handle(self, message, generator):
        try:
            message_content = message.text
            parse_command(message_content)
            if message_content in commands:
                commands[message_content](generator)
        except:
            self.alive = False
