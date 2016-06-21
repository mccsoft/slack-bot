import pykka
from slack_utils import wrapper
from collections import namedtuple
import requests
from dateutil import parser
import json


def get_color(predicate):
    return "good" if predicate else "danger"


def act(url):
    try:
        response = requests.get(url)
        raw_content = response.content.decode('utf-8')
        live_report = json.loads(raw_content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        wrapper.print("", title="{0} - {1}".format(live_report.ServiceName, live_report.Version), color="good",
                      fallback="Service status")

        wrapper.print("", title="RabbitMq", color=get_color(live_report.IsRabbitMqAlive), fallback="Rabbit status")
        wrapper.print("", title="Database", color=get_color(live_report.IsDatabaseAlive),
                      fallback="Database status")

        for transmission in live_report.TransmissionStatistics:
            date = parser.parse(transmission.TransmissionsDate)
            title = "Transmission for: {0}".format(date.strftime("%Y-%B-%d"))
            text = "Published {0} messages, failed {1}. \n Consumed {2} message, failed {3}".format(
                transmission.SuccedPublishedMessage, transmission.FailedToPublishedMessage,
                transmission.ConsumedMessage, transmission.FailedToConsumeMessage)
            wrapper.print("", text=text, title=title, fallback="title")
    except:
        wrapper.print("", title="Service is on url {0} is unavailable".format(url), color="danger")


class ServiceStatusActor(pykka.ThreadingActor):
    def on_receive(self, message):
        message_content = message.get("text", None)

        if message_content == "!status":
            act("http://localhost:5000")
