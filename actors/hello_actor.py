import pykka
from slack_utils import wrapper


class HelloActor(pykka.ThreadingActor):

    def on_receive(self, message):
        wrapper.print("Somebody call me? To know what i can type !info")
