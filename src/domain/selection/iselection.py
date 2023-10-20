from abc import ABCMeta, abstractclassmethod


class SelectionInterface(metaclass=ABCMeta):
    
    @abstractclassmethod
    def select(self,population,scores,minimize=True):
        '''Select'''
        raise NotImplementedError
