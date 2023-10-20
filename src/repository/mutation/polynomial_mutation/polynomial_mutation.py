
from src.domain.mutations.imutation import MutationInterface
from numpy import random

class PolynomialM(MutationInterface):

    def mutate(self,ind):
        
        for i in range(len(ind)):
            # check for a mutation
            if random.rand() < self.r_mut:
                # flip the bit
                ind[i] = 1 - ind[i]