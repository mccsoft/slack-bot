from requests.auth import HTTPBasicAuth
import requests
from Config import teamcity_creds

url = "http://teamcity.mcc-tomsk.de/httpAuth/app/rest/buildQueue"
xml = """<build>
            <buildType id="{0}"/>
         </build>"""

headers = {'Content-Type': 'application/xml'}


def trigger_build(build_id):
    body = xml.format(build_id)
    response = requests.post(url, data=body, headers=headers, auth=HTTPBasicAuth(teamcity_creds["login"], teamcity_creds["password"]))

    return response.status_code
