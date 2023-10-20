from src.domain.selection import SelectionInterface
import random

class RandomSelection(SelectionInterface):

    def select(self, population, scores, minimize):
        # Randomly select one individual from the population
        selected_index = random.randint(0, len(population) - 1)
        selected_individual = population[selected_index]
        
        return selected_individual