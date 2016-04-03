import json
from collections import namedtuple


class ConfigProvider:

    def __init__(self):
        with open('appsettings.json') as config_file:
            self.config = json.load(config_file, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            self.token = self.config.token

    def user_credentials(self):
        return self.config.teamcity_credentials.login, self.config.teamcity_credentials.password

    def bot_settings(self):
        return self.config.bot_settings.bot_name, self.config.bot_settings.channel_name


config_provider = ConfigProvider()