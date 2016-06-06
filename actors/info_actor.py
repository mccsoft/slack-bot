import pykka
from slack_utils import wrapper
from commands import commands


class InfoActor(pykka.ThreadingActor):

    def on_receive(self, message):
        wrapper.print("", title="I can do some cool stuff actually!")

        for key in commands.keys():
            if key != "!poling commands -avp -d -f":
                wrapper.print("", title=key)
