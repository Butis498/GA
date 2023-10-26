from src.domain.mutations import MutationInterface
import numpy as np

class DEMutation(MutationInterface):

    def mutate(self,selected,bounds):

        return  np.array(selected[0]) + self.r_mut * (np.array(selected[1]) - np.array(selected[2]))