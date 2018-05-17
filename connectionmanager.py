from stem import Signal
from stem.control import Controller


class Connectionmanager:

    def __init__(self):
        self.newId = self.get_newId(8118)


    def get_newId(self, port_number):

        with Controller.from_port(port=port_number) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

