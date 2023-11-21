from src.domain.selection import SelectionInterface
import random
import numpy as np

class DESelection(SelectionInterface):

    def select(self,population,minimize=True):

        result = random.sample(population[:len(population)],3)

        result[0] = population[0]

        return result
    

    def stochastic_ranking(self,population,scores_fucntion,scores_penalty):

        ranked = population.copy()
        pf = 0.2

        for _ in range(len(ranked)):
            swap = False
            for i in range(len(population)-2):
                u = random.random()
                if (scores_penalty[i] == scores_penalty[i+1] == 0) or u < pf:
                    if scores_fucntion[i] > scores_fucntion[i+1]:
                        temp = ranked[i]
                        ranked[i] = ranked[i+1]
                        ranked[i+1] = temp
                        swap = True
                else:

                    if scores_penalty[i] > scores_penalty[i+1]:
                        temp = ranked[i]
                        ranked[i] = ranked[i+1]
                        ranked[i+1] = temp
                        swap = True

            if not swap:
                break

        return ranked

        

            

