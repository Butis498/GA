from src.domain.selection import SelectionInterface
import random


class RandomSelection(SelectionInterface):

    def select(self, population, scores, minimize):

        ind = random.randint(0,len(population)-1)
        return population[ind]

