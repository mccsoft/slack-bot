teamcity_commands =["build"]

teamcity_parameters = ["WebAPI"]


def execute_command(command, parameter):
    pass


def parse_command(message_content):
    print(message_content[0])
    if message_content[0] == "!":
        array_of_words = message_content[1:].split()
        if array_of_words[0] in teamcity_commands:
            if array_of_words[1] in teamcity_parameters:
                execute_command(array_of_words[0], array_of_words[1])
