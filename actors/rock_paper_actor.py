import pykka
from enum import Enum
from random import shuffle
from slack_utils import wrapper


variables = ["rock", "paper", "scissors"]


def am_i_win(my_bet, opponents_bet):
    if my_bet == "rock":
        if opponents_bet == "scissors":
            wrapper.print("", title="I definitely crush your scissors with rock!", color="danger")
            return
        else:
            wrapper.print("", title="Oh no i loose, i was betting on rock!", color="good")
            return

    if my_bet == "scissors":
        if opponents_bet == "paper":
            wrapper.print("", title="Ha ha scissors is bigger then paper i win!", color="danger")
            return
        else:
            wrapper.print("", title="My scissors is useless against your rock!", color="good")
            return

    if opponents_bet == "rock":
        wrapper.print("", title="Paper is't a weakest bet i win!", color="danger")
    else:
        wrapper.print("", title="Stop cutting my paper", color="good")


def act_not_started(message):
    wrapper.print("Lets play rock paper scissors i would't cheat!")

    wrapper.print("", title="Rock paper scissors")

    wrapper.print("", title="1")
    wrapper.print("", title="2", color="warning")
    wrapper.print("", title="3", color="good")


def act_answer(message):
    shuffle(variables)
    bet = variables[0]

    if bet == message:
        wrapper.print("", title="It's a draw i bet you can do better", color='warning')
    else:
        am_i_win(bet, message)


class RockPaperState(Enum):
        not_started = 0,
        waiting_for_answer = 1


class RockPaperActor(pykka.ThreadingActor):

    def __init__(self):
        super(RockPaperActor, self).__init__()
        self.state = RockPaperState.not_started

    def on_receive(self, message):
        message_content = message.get("text", None)

        if self.state is RockPaperState.not_started:
            if message_content == "!rock":
                act_not_started(message)
                self.state = RockPaperState.waiting_for_answer

        if self.state is RockPaperState.waiting_for_answer:
            if message_content in variables:
                act_answer(message)
                self.state = RockPaperState.not_started

