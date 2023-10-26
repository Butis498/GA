
from src.domain.mutations.imutation import MutationInterface
from numpy import random

class PolynomialM(MutationInterface):

    def mutate(self, ind,bounds):
        self.eta = 4
        for i in range(len(ind)):
            if random.rand() < self.r_mut:
                u = random.rand()
                delta = min(ind[i] - bounds[i][0], bounds[i][1] - ind[i])
                if u <= 0.5:
                    delta_q = (2.0 * u) ** (1.0 / (self.eta + 1)) - 1.0
                else:
                    delta_q = 1.0 - (2.0 * (1.0 - u)) ** (1.0 / (self.eta + 1))
                ind[i] += delta * delta_q
