from journey.interface.ViewInterface import ViewInterface
from journey.src.decorator import *

class Journey:

    def __init__(self, View: ViewInterface):
        self.__view = View()
        self.__view.create()

    @strict
    def run(self):
        print("data")