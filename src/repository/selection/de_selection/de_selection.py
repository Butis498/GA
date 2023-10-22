from src.domain.selection import SelectionInterface
import random

class DESelection(SelectionInterface):

    def select(self,population,scores,minimize=True):
        return random.sample(population, 3)