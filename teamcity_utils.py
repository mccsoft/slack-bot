from pyteamcity import TeamCity
from config import teamcity_creds

def get_build_ids():
    tc = TeamCity(teamcity_creds["login"], teamcity_creds["password"], "teamcity.mcc-tomsk.de")

    build_ids = [build['id'] for build in tc.get_all_build_types()['buildType']]

    return "\n".join(build_ids)
