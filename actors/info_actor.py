import pykka
from slack_utils import wrapper
from commands import commands


class InfoActor(pykka.ThreadingActor):

    def on_receive(self, message):
        message_content = message.get("text", None)

        if message_content == "!info":
            wrapper.print("", title="I can do some cool stuff actually!")

            for command in commands:
                if command != "!poling commands -avp -d -f":
                    wrapper.print("", title=command)
