import pykka
from slack_utils import wrapper
from teamcity.teamcity_utils import get_build_ids


class BuildListActor(pykka.ThreadingActor):

    def on_receive(self, message):
        message_content = message.get("text", None)

        if message_content == "!builds":
            build_ids = get_build_ids()
            wrapper.print("", title="\n\n".join(build_ids))
