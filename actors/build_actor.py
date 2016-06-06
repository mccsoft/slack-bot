import pykka
from slack_utils import wrapper
import re
from teamcity.teamcity_requests import process_build


COMMNAD_PATTERN = '!build \w+'


class BuildActor(pykka.ThreadingActor):

    def __init__(self):
        super(BuildActor, self).__init__()
        self.reg_exp = re.compile(COMMNAD_PATTERN)

    def on_receive(self, message):
        message_content = message.get("text", None)

        if message_content == "!build":
            wrapper.print("Please, specify which build to start.")

        if self.reg_exp.match(message_content):
            process_build(message_content.split()[1])


