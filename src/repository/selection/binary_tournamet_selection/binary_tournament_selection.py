from src.domain.selection.iselection import SelectionInterface
import random

class BinaryTS(SelectionInterface):


    def select(self,population, scores,minimize:True):
        # Randomly select two distinct individuals
        index1, index2 = random.sample(range(len(population)), 2)
        
        # Compare their fitness values and select the better one
        if scores[index1] > scores[index2] and not minimize:
            return population[index1]
        else:
            return population[index2]