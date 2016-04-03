from pyteamcity import TeamCity
from config_provider import config_provider

login, password = config_provider.user_credentials()


def get_build_ids():
    tc = TeamCity(login, password, "teamcity.mcc-tomsk.de")

    return [build['id'] for build in tc.get_all_build_types()['buildType']]
