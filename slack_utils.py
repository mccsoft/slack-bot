from slacker import Slacker
from config_provider import config_provider

_, channel_name = config_provider.bot_settings()

slack = Slacker(config_provider.token)


def print_to_slack(message):
    slack.chat.post_message(channel_name, message, 'bombila')


def get_channel_id(name):
    for channel in slack.channels.list().body['channels']:
        if channel['name'] == name:
            return channel['id']
