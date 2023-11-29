
from abc import ABCMeta, abstractclassmethod


class MutationInterface(metaclass=ABCMeta):

    def __init__(self,r_mut=1.0,eta=6) -> None:
        self.r_mut = r_mut
        self.eta = eta
    
    @abstractclassmethod
    def mutate(self,individual,bounds):
        '''Mutate'''
        raise NotImplementedError
