import time
from slack_utils import wrapper
import threading


users = ["anp", "sbu", "kalesin"]

class AvpHandler:
    def __init__(self):
        self.alive = True
        threading.Thread(target=self.secrete_command).start()

    def is_alive(self):
        return self.alive

    def handle(self, message, generator):
        if message.user_name() == "avp":
            wrapper.print("hubble-bubble")
            self.alive = False
        elif message.user_name() in users and message.text == "!ShutUp":
            wrapper.print("Ok ok, you should't be so rude")
            self.alive = False

    def secrete_command(self):
        while self.alive:
            wrapper.print("Are <@U072ECBRB> there?")
            time.sleep(2)
