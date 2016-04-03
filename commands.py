from handlers.avp_secret_handler import AvpHandler
from handlers.rock_paper_handler import RockPaperHandler
from slack_utils import wrapper
from teamcity.teamcity_utils import get_build_ids


def hello(_):
    wrapper.print("Somebody call me? To know what i can type !info")


def info(_):
    wrapper.print("", title="I can do some cool stuff actually!")

    for key in commands.keys():
        if key != "!poling commands -avp -d -f":
            wrapper.print("", title=key)


def secrete_command(generator):
    generator.add_handler(AvpHandler())


def builds(_):
    build_ids = get_build_ids()
    wrapper.print("", title="\n\n".join(build_ids))


def empty_command(_):
    pass


def rock(generator):
    generator.add_handler(RockPaperHandler())

commands = {"bot": hello,
            "!info": info,
            "!builds": builds,
            "!build <Build Type Id>": empty_command,
            "!rock": rock,
            "!poling commands -avp -d -f": secrete_command}