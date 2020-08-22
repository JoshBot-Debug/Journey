from journey.interface.ViewInterface import ViewInterface

class View(ViewInterface):
    
    def __init__(self):
        print("view init")

    def create(self):
        print("Created")