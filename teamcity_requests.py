from requests.auth import HTTPBasicAuth
import requests
from Config import teamcity_creds
from bs4 import BeautifulSoup
from SlackUtils import print_to_slack
import time

url = "http://teamcity.mcc-tomsk.de/httpAuth/app/rest/buildQueue"
xml = """<build>
            <buildType id="{0}"/>
         </build>"""

headers = {'Content-Type': 'application/xml'}


def trigger_build(build_id):
    body = xml.format(build_id)
    response = requests.post(url, data=body, headers=headers, auth=HTTPBasicAuth(teamcity_creds["login"], teamcity_creds["password"]))

    return response


def observe_build_status(url):
    while True:
        response = requests.get("http://teamcity.mcc-tomsk.de" + url, auth=HTTPBasicAuth(teamcity_creds["login"],
                                                                                         teamcity_creds["password"]))

        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.prettify())
        if soup.build['status'] == "FAILURE":
            print_to_slack(soup.statustext)
            break

        if soup.build['status'] == "SUCCESS":
            print_to_slack(soup.statustext)
            break

        print_to_slack(soup.build['status'])
        print_to_slack(soup.statustext)
        time.sleep(30)

