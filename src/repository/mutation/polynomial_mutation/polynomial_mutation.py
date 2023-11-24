
from src.domain.mutations.imutation import MutationInterface
from numpy import random
import time
import numpy as np

class PolynomialM(MutationInterface):

    def mutate(self,ind, bounds):

        self.eta = 6
        for i in range(len(ind)):
            # Check if mutation should be applied
            if np.random.rand() > self.r_mut:
                continue

            # Select random bounds for the mutation
            lower_bound, upper_bound = bounds[i]

            # Calculate delta values
            delta1 = (upper_bound - ind[i])
            delta2 = (ind[i] - lower_bound)

            # Generate random delta values
            if np.random.rand() <= 0.5:
                y = ind[i] + delta1 * pow(-np.random.rand(), 1.0 / self.eta)
            else:
                y = ind[i] - delta2 * pow(-np.random.rand(), 1.0 / self.eta)

            if np.iscomplex(y):
                y = np.real(y)

            # Ensure the mutated value is within the bounds
            y = max(lower_bound, min(upper_bound, y))

            # Apply the mutation
            ind[i] = y

        return ind