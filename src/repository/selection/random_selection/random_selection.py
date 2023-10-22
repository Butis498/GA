from src.domain.selection import SelectionInterface
import random

class RandomSelection(SelectionInterface):

    def select(self, population, scores, minimize):

        if not minimize:
            total_fitness = sum(scores)

            # Check if total_fitness is zero
            if total_fitness == 0:
                return random.choice(population)

            cumulative_probabilities = [sum(scores[:i + 1]) / total_fitness for i in range(len(population))]
            random_number = random.uniform(0, 1)

            for i, probability in enumerate(cumulative_probabilities):
                if random_number <= probability:
                    return population[i]
        else:
            total_inverted_fitness = sum(1.0 / score for score in scores)

            # Check if total_inverted_fitness is zero
            if total_inverted_fitness == 0:
                return random.choice(population)

            cumulative_inverted_probabilities = [sum(1.0 / score for score in scores[:i + 1]) / total_inverted_fitness for i in range(len(population))]
            random_number = random.uniform(0, 1)

            for i, inverted_probability in enumerate(cumulative_inverted_probabilities):
                if random_number <= inverted_probability:
                    return population[i]
