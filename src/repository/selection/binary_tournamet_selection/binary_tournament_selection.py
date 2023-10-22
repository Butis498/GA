from src.domain.selection.iselection import SelectionInterface
import random

class BinaryTS(SelectionInterface):


    def select(self,population, scores,minimize:True):
        # Randomly select two distinct individuals
        index1, index2 = random.sample(range(len(population)), 2)
        
        # Compare their fitness values and select the better one
        if minimize:
            if scores[index1] < scores[index2]:
                return population[index1]
            return population[index2]
        else:
            if scores[index1] > scores[index2]:
                return population[index1]
            return population[index2]