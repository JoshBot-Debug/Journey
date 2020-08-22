import abc

class ViewInterface(metaclass=abc.ABCMeta):
    """ This interface makes sure that all View objects have the method create """
    
    @abc.abstractmethod
    def create(self): pass