from slacker import Slacker
from config import token

slack = Slacker(token)


def print_to_slack(message):
    slack.chat.post_message("#hackaton-bot", message, 'bombila')


def get_channel_id(name):
    for channel in slack.channels.list().body['channels']:
        if channel['name'] == name:
            return channel['id']
