from teamcity_requests import trigger_build, observe_build_status
from slack_utils import wrapper
from bs4 import BeautifulSoup
import threading

teamcity_commands =["build"]

teamcity_parameters = [""]

build_ids = ["SomnocloudWebAPI_Master"]

def execute_command(command, parameter):
    if command == "build":
        if parameter in build_ids:
            response = trigger_build(parameter)

            parse_response(response)


def parse_response(response):
    soup = BeautifulSoup(response.text)
    if response.status_code == 200:
        wrapper.print("", title="Build triggered", color="good", title_link=soup.build["weburl"])

        threading.Thread(target=observe_build_status, args=[soup.build['href']]).start()
    else:
        wrapper.print("Build triggering error : " + response.status_code, title="Failure!", color="danger")


def parse_command(message_content):
    print(message_content[0])
    if message_content[0] == "!":
        array_of_words = message_content[1:].split()
        if array_of_words[0] in teamcity_commands:
            if array_of_words[1] in build_ids:
                execute_command(array_of_words[0], array_of_words[1])
