from slacker import Slacker
from config_provider import config_provider
bot_name, channel_name = config_provider.bot_settings()

slack = Slacker(config_provider.token)


def get_channel_id(name):
    for channel in slack.channels.list().body['channels']:
        if channel['name'] == name:
            return channel['id']


class SlackWrapper:

    def __init__(self):
        self.slack = Slacker(config_provider.token)

    def print(self, message, **kwargs):
        self.slack.chat.post_message(channel_name, message, bot_name, attachments=[kwargs])

wrapper = SlackWrapper()
