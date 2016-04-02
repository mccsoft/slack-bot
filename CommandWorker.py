from teamcity_requests import trigger_build
from SlackUtils import print_to_slack

teamcity_commands =["build"]

teamcity_parameters = [""]

build_ids = ["SomnocloudWebAPI_Master"]

def execute_command(command, parameter):
    if command == "build":
        if parameter in build_ids:
            response = trigger_build(parameter)

            if response.status_code == 200:
                print_to_slack("Build triggered.")
                print(response)

            if response.status_code != 200:
                print_to_slack("Build triggering error : " + response.status_code)
                print(response)



def parse_command(message_content):
    print(message_content[0])
    if message_content[0] == "!":
        array_of_words = message_content[1:].split()
        if array_of_words[0] in teamcity_commands:
            if array_of_words[1] in build_ids:
                execute_command(array_of_words[0], array_of_words[1])
