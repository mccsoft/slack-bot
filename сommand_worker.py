import threading
from bs4 import BeautifulSoup
from teamcity.teamcity_requests import trigger_build, observe_build_status
from slack_utils import wrapper
from teamcity.teamcity_utils import get_build_ids

teamcity_commands = ["build"]


def execute_teamcity_command(command):
    if command[1] in get_build_ids():
        response = trigger_build(command[1])
        parse_response(response)


def parse_response(response):
    soup = BeautifulSoup(response.text)
    if response.status_code == 200:
        wrapper.print("", title="Build triggered", color="good", title_link=soup.build["weburl"])

        threading.Thread(target=observe_build_status, args=[soup.build['href']]).start()
    else:
        wrapper.print("Build triggering error : " + response.status_code, title="Failure!", color="danger")
