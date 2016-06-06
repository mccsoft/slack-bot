from requests.auth import HTTPBasicAuth
import requests
from bs4 import BeautifulSoup
from slack_utils import wrapper
import time
from config_provider import config_provider
import threading


login, password = config_provider.user_credentials()

url = "http://teamcity.mcc-tomsk.de/httpAuth/app/rest/buildQueue"
xml = """<build>
            <buildType id="{0}"/>
         </build>"""

headers = {'Content-Type': 'application/xml'}


def trigger_build(build_id):
    body = xml.format(build_id)
    response = requests.post(url, data=body, headers=headers, auth=HTTPBasicAuth(login, password))

    return response


def get_color(status_text):
    return "good" if status_text.lower() == "success" else "danger"


def observe_build_status(url):
    while True:
        response = requests.get("http://teamcity.mcc-tomsk.de" + url, auth=HTTPBasicAuth(login, password))
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.build['state'] == "queued":
            wrapper.print("Build agents are not ready waiting for them!", titile="Build queued", color="warning")
            time.sleep(60)

        if soup.build['state'] == "running":
            wrapper.print("Build is currently running", title="Running a build", color="#439FE0")
            time.sleep(60)

        if soup.build['state'] == "finished":
            wrapper.print(("Build Finished with status text: {0}".format(soup.statustext.text)), title="Finished!", color=get_color(soup.statustext.text))
            break


def parse_response(response):
    soup = BeautifulSoup(response.text)
    if response.status_code == 200:
        wrapper.print("", title="Build triggered", color="good", title_link=soup.build["weburl"])

        threading.Thread(target=observe_build_status, args=[soup.build['href']]).start()
    else:
        wrapper.print("Build triggering error : " + response.status_code, title="Failure!", color="danger")


def process_build(build_id):
    response = trigger_build(build_id)
    parse_response(response)