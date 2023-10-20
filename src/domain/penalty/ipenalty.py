from abc import ABCMeta, abstractclassmethod


class PenaltyInterface(metaclass=ABCMeta):
    
    @abstractclassmethod
    def punish(sefl,ind):
        '''punish individual'''
        return 0
    
    @abstractclassmethod
    def penalty_function(self,ind):
        '''Penalty function'''
        return 0
