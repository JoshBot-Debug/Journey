from journey.interface.ViewInterface import ViewInterface

class Journey:
    """ This is the main controller where all the action comes together """

    def __init__(self, View: ViewInterface):
        self.__view = View()


    def mainloop(self):
        """ This method must be called in order to start the view object's main loop """
        self.__view._mainloop()