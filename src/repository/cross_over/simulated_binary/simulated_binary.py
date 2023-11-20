from src.domain.cross_over import CrossOverInterface
import random
import numpy as np
import time
class SimulatedBC(CrossOverInterface):

    def cross_over(self, parents, bounds):
        parent1, parent2 = parents
        parent1 = np.array(parent1)
        parent2 = np.array(parent2)
        etc = 15

        if np.random.rand() > self.r_cross:
            return parent1, parent2

        u = random.random()

        if self.r_cross <= 0.5:
            beta = (2*u)**(1/(etc+1))
        else:
            beta = (1/(2*(1-u)))**(1/(etc+1))

        if np.linalg.norm(parent2) < np.linalg.norm(parent1):
            parent1, parent2 = parent2, parent1

        off1 = 0.5 * ((1 + beta) * parent1 + (1 - beta) * parent2)
        off2 = 0.5 * ((1 - beta) * parent1 + (1 + beta) * parent2)

        off1 = np.array([min(max(x, bounds[i][0]), bounds[i][1]) for i, x in enumerate(off1)])
        off2 = np.array([min(max(x, bounds[i][0]), bounds[i][1]) for i, x in enumerate(off2)])

        return [off1, off2]
