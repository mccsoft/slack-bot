from config_provider import config_provider
from message_generator import MessageGenerator
from actors.build_actor import BuildActor
from actors.rock_paper_actor import RockPaperActor
from actors.service_status_actor import ServiceStatusActor
from actors.hello_actor import HelloActor
from actors.build_list_actor import BuildListActor
from actors.info_actor import InfoActor

class Bot:

    def __init__(self):
        self.token = config_provider.token
        self.generator = MessageGenerator(self.token)
        HelloActor.start()
        InfoActor.start()
        BuildListActor.start()
        ServiceStatusActor.start()
        RockPaperActor.start()
        BuildActor.start()

    def run(self):
        self.generator.run()
