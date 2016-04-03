import time
from slack_utils import wrapper


class AvpHandler:
    def __init__(self):
        self.alive = True

        while self.alive:
            self.secrete_command()

    def is_alive(self):
        return self.alive

    def handle(self, message, generator):
        if message.user_name == "sbu":
            wrapper.print("hubble-bubble")
            self.alive = False

    def secrete_command(self):
        wrapper.print("Are <@U072ECBRB> there?")
        time.sleep(2)
