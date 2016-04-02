import time
from slackclient import SlackClient
from slacker import Slacker

slack = Slacker("xoxp-3112620471-7040594676-31499489488-82fa270292")


token = "xoxp-3112620471-7040594676-31499489488-82fa270292"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        message = sc.rtm_read()
        if len(message) != 0:
            unpacked = message[0]
            if "text" in unpacked and unpacked["text"] == "bot":
                slack.chat.post_message('#hackaton-bot', 'Somebody call me?')
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")