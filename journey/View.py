import cmd

from journey.interface.ViewInterface import ViewInterface

class View(cmd.Cmd,ViewInterface):
    """ Journey view object """

    def preloop(self):
        print ('cmdloop')


    def do_greet(self, person):
        """greet [person] Greet the named person"""
        if person: print ("hi,", person) else: print ('hi')


    def do_quit(self, line):
        return True


    def _mainloop(self):
        self.cmdloop()
        