from requests.auth import HTTPBasicAuth
import requests
from bs4 import BeautifulSoup
from slack_utils import print_to_slack
import time
from config_provider import config_provider

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


def observe_build_status(url):
    while True:
        response = requests.get("http://teamcity.mcc-tomsk.de" + url, auth=HTTPBasicAuth(login, password))
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.build['state'] == "queued":
            print_to_slack("Build queued")
            time.sleep(30)

        if soup.build['state'] == "running":
            print_to_slack("Running a buils")
            time.sleep(30)

        if soup.build['state'] == "finished":
            print_to_slack("Build Finished with status text: {0}".format(soup.statustext.text))
            break