from abc import ABCMeta, abstractclassmethod

class CrossOverInterface(metaclass=ABCMeta):

    def __init__(self,r_cross:float = 1, n_parents=2,n_offspring=1,eta=15) -> None:
        self.r_cross = r_cross
        self.eta = eta
        self.n_parents = n_parents
        self.n_offspring = n_offspring
        if n_offspring == None:
            self.n_offspring = 1
        

    @abstractclassmethod
    def cross_over(self,parents):
        '''Cross Over'''
        raise NotImplementedError


    