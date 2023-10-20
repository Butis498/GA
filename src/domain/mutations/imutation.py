
from abc import ABCMeta, abstractclassmethod


class MutationInterface(metaclass=ABCMeta):

    def __init__(self,r_mut=1.0):
        self.r_mut = r_mut
    
    @abstractclassmethod
    def mutate(self,individual):
        '''Mutate'''
        raise NotImplementedError
