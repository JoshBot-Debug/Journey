from journey.interface.ViewInterface import ViewInterface

class Journey:
    """ This is the main controller where all the action comes together """

    def __init__(self, View: ViewInterface):
        self.__view = View()
        self.__view._create()


    def mainloop(self):
        self.__view._mainloop()