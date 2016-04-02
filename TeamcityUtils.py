from pyteamcity import TeamCity
from Config import teamcity_creds

def get_project_names():
    tc = TeamCity(teamcity_creds["login"], teamcity_creds["password"], "teamcity.mcc-tomsk.de")

    project_names = [project['name'] for project in tc.get_projects()["project"]]

    return "\n".join(project_names)