from src.domain.population.ipopulation import PopulationInterface
from src.domain.encoding.iencoding import EncodingInterface
from numpy.random import randint

class BinaryPopulation(PopulationInterface):

    def generate(n_ind,encoding:EncodingInterface):

        return [randint(0, 2,encoding.n_bits *len(encoding.bounds)).tolist() for _ in range(n_ind)]
    
    def update(children):
        return children