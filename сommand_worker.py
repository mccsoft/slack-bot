from teamcity_requests import trigger_build, observe_build_status
from slack_utils import wrapper
from bs4 import BeautifulSoup
from teamcity_utils import get_build_ids
from slack_utils import wrapper
import threading

teamcity_commands = ["build"]
build_ids = get_build_ids()


def execute_teamcity_command(command):
    if len(command) > 0:
        if command[0] == "build":

            if len(command) == 1:
                wrapper.print("Please, specify which build to start.")
                return

            if command[1] in build_ids:
                response = trigger_build(command[1])
                parse_response(response)


def parse_response(response):
    soup = BeautifulSoup(response.text)
    if response.status_code == 200:
        wrapper.print("", title="Build triggered", color="good", title_link=soup.build["weburl"])

        threading.Thread(target=observe_build_status, args=[soup.build['href']]).start()
    else:
        wrapper.print("Build triggering error : " + response.status_code, title="Failure!", color="danger")


def parse_command(message_content):
    if len(message_content):
        if message_content[0] == "!":
            array_of_words = message_content[1:].split()
            if array_of_words[0] in teamcity_commands:
                execute_teamcity_command(array_of_words)
