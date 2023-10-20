from src.domain import CrossOverInterface
import random

class SinglePointCO(CrossOverInterface):

    def __init__(self):
        pass

    def cross_over(parents):

        parent1,parent2 = parents[0],parents[1]
        # Ensure that the parents have the same length
        if len(parent1) != len(parent2):
            raise ValueError("Parent chromosomes must have the same length.")

        # Choose a random crossover point
        crossover_point = random.randint(1, len(parent1) - 1)

        # Create offspring by swapping segments
        c1 = parent1[:crossover_point] + parent2[crossover_point:]
        c2 = parent2[:crossover_point] + parent1[crossover_point:]

        return [c1, c2]



