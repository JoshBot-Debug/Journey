import abc

class ViewInterface(metaclass=abc.ABCMeta):
    """ This interface makes sure that all View objects have the method _mainloop """

    @abc.abstractmethod
    def _mainloop(self): pass