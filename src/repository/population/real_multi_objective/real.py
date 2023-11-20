from src.domain.population.ipopulation import PopulationInterface
from src.domain.encoding.iencoding import EncodingInterface
import random


class Individual():
    def __init__(self,value) -> None:
        self.rank = 0
        self.crowding_distance = 0
        self.value = value
        self.fitness = []

    def dominates(self,other_ind,minimize=True):

        if (self.rank < other_ind.rank) or ((self.rank == other_ind.rank) and (self.crowding_distance > other_ind.crowding_distance)):
            return True if minimize else False
        return False if minimize else True


class RealPMO(PopulationInterface):

    def __init__(self) -> None:
        super().__init__()
        
        

    def generate(self,n_ind:int,encoding:EncodingInterface):
       
       bounds = encoding.bounds
       ind_g = lambda bounds:[random.uniform(l,r) for l,r in bounds]

       return  [Individual(ind_g(bounds)) for _ in range(n_ind)]
    

    def update(self,children,pop):
        return children + pop