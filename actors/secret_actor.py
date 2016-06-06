import pykka
from enum import Enum
from slack_utils import wrapper


class SecreteActorState(Enum):
    not_started = 0,
    waiting_for_secret = 1


class SecreteActor(pykka.ThreadingActor):
    def __init__(self):
        super(SecreteActor, self).__init__()
        self.state = SecreteActorState.not_started

    def on_receive(self, message):
        message_content = message.get("text", None)

        if message_content == "!poling commands -avp -d -f":
            self.state = SecreteActorState.waiting_for_secret

        if self.state == SecreteActorState.waiting_for_secret:
            wrapper.print("Are <@U072ECBRB> there?")
