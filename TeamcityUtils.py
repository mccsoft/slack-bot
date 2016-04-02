from pyteamcity import TeamCity


def get_project_names():
    tc = TeamCity("", "", "teamcity.mcc-tomsk.de")

    project_names = [project['name'] for project in tc.get_projects()]

    return "\n".join(project_names)