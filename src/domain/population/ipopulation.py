from abc import ABCMeta, abstractclassmethod
from src.domain.encoding.iencoding import EncodingInterface

class PopulationInterface(metaclass=ABCMeta):
    
    @abstractclassmethod
    def generate(self,n_individuals:int,encoding:EncodingInterface):
        '''Select'''
        raise NotImplementedError

    @abstractclassmethod
    def update(self,children:list):
        raise NotImplementedError