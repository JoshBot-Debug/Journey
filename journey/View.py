import cmd

from journey.interface.ViewInterface import ViewInterface

class View(cmd.Cmd,ViewInterface):
    
    def __init__(self):
        print("view init")

    def _create(self):
        print("Created")

    def _mainloop(self):
        