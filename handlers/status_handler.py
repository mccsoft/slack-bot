from collections import namedtuple
from slack_utils import wrapper
import requests
import json
import dateutil.parser as date_parser


def get_color(predicate):
        return "good" if predicate else "danger"


class StatuMessageHandler:

    def __init__(self):
        response = requests.get("http://localhost:5000")
        raw_content = response.content.decode('utf-8')
        live_report = json.loads(raw_content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        wrapper.print("", title="{0} - {1}".format(live_report.ServiceName, live_report.Version), color="good", fallback="Service status")

        wrapper.print("", title="RabbitMq", color=get_color(live_report.IsRabbitMqAlive), fallback="Rabbit status")
        wrapper.print("", title="Database", color=get_color(live_report.IsDatabaseAlive), fallback="Database status")

        for transmission in live_report.TransmissionStatistics:
            date = date_parser.parse(transmission.TransmissionsDate)
            title = "Transmission for: {0}".format(date.strftime("%Y-%B-%d"))
            text = "Published {0} messages, failed {1}. \n Consumed {2} message, failed {3}".format(transmission.SuccedPublishedMessage, transmission.FailedToPublishedMessage, transmission.ConsumedMessage, transmission.FailedToConsumeMessage)
            wrapper.print("", text=text, title=title, fallback="title")

        self.alive = False

    def is_alive(self):
        return self.alive

    def handle(self, message, generator):
        pass
