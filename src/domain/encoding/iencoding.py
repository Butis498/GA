from abc import ABCMeta, abstractclassmethod
import random

class EncodingInterface(metaclass=ABCMeta):

    def __init__(self,bounds:list=[]):
        self.bounds = bounds

        if len(bounds) == 0:

            raise IndexError('Bounds not defined')
    
    @abstractclassmethod
    def decode(self,individual):
        '''test'''
        raise NotImplementedError
