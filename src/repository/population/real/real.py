from src.domain.population.ipopulation import PopulationInterface
from src.domain.encoding.iencoding import EncodingInterface
import random

class RealP(PopulationInterface):

    def generate(self,n_ind:int,encoding:EncodingInterface):
       
       bounds = encoding.bounds
       ind_g = lambda bounds:[random.uniform(l,r) for l,r in bounds]

       return  [ind_g(bounds) for _ in range(n_ind)]
    

    def update(self,children):
        return children