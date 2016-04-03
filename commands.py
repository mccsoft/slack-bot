from teamcity_utils import get_build_ids
from slack_utils import wrapper
from rock_paper_scissors import RockPaperHandler


def hello(generator):
    wrapper.print("Somebody call me? To know what i can type !info")


def info(generator):
    wrapper.print("", title="I can do some cool stuff actually!")

    for key in commands.keys():
        wrapper.print("", title=key)


def secrete_command(generator):
    wrapper.print("Are <@U072ECBRB> there?")


def builds(generator):
    for build_id in get_build_ids():
        wrapper.print("", title=build_id)


def empty_command(generator):
    pass


def rock(generator):
    generator.add_handler(RockPaperHandler())

commands = {"bot": hello,
            "!info": info,
            "!builds": builds,
            "!build <Build Type Id>": empty_command,
            "!rock": rock}