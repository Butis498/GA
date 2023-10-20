from abc import ABCMeta, abstractclassmethod


class FitnessInterface(metaclass=ABCMeta):
    
    @abstractclassmethod
    def test(self):
        '''test'''
        pass
