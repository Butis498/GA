from src.domain.cross_over import CrossOverInterface
import random
import numpy as np

class SimulatedBC(CrossOverInterface):

    def cross_over(self,parents,bounds=[]):

        p1,p2 = parents


        p1 = np.array(p1)
        p2 = np.array(p2)
        eta=20
        
        if np.random.random() > self.r_cross:
            return p1, p2

        u = np.random.rand()

        if u <= 0.5:
            beta = (2*u)**(1/(eta+1))
        else:
            beta = (1/(2*(1-u)))**(1/(eta+1))

        off1 = 0.5*((p1+p2)-beta*np.linalg.norm(p2-p1))
        off2 = 0.5*((p1+p2)+beta*np.linalg.norm(p2-p1))

        off1 = np.array([min(max(x, bounds[i][0]), bounds[i][1]) for i,x in enumerate(off1)])
        off2 = np.array([min(max(x, bounds[i][0]), bounds[i][1]) for i,x in enumerate(off2)])

        return [off1, off2]






