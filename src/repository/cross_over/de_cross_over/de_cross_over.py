from src.domain.cross_over import CrossOverInterface
import random
import numpy as np

class DECrossOver(CrossOverInterface):

    def cross_over(self,ind,u):
        n = len(ind)
        j = set()
        rand_ = random.randint(1, n-1)
        new_i = ind.copy()

        new_i[rand_] = u[rand_]
        for i in range(n):
            if random.random() < self.r_cross :  
                new_i[i] = u[i]

        return new_i