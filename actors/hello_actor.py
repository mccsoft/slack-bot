import pykka
from slack_utils import wrapper


class HelloActor(pykka.ThreadingActor):

    def on_receive(self, message):
        message_content = message.get("text", None)

        if message_content == "bot":
            wrapper.print("Somebody call me? To know what i can type !info")
