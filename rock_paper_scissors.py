from slack_utils import wrapper
from random import shuffle

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


class RockPaperHandler:

    def __init__(self):
        self.alive = True

        wrapper.print("Lets play rock paper scissors i would't cheat!")

        wrapper.print("", title="Rock paper scissors")

        wrapper.print("", title="1")
        wrapper.print("", title="2", color="warning")
        wrapper.print("", title="3", color="good")

    def is_alive(self):
        return self.alive

    def handle(self, message, generator):
        if message.text in variables:
            shuffle(variables)
            first = variables[0]

            if first == message.text:
                wrapper.print("It's a draw i bet you can do better", color='warning')
            else:
                am_i_win(first, message.text)

            self.alive = False
