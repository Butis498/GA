
from src.genetic_algorithm.genetic_alorithm import GeneticAlgorithm
from src.repository.population import Individual
from src.nsga import NSGAII_SORTING
import pandas as pd
from src.differential_evolution import DifferentialEvolution


class NSDE(DifferentialEvolution):

    def fast_non_dominated_sort(self, population,objectives):


        columns = ['f'+str(i+1) for i in range(self.n_objectives)]
        df = pd.DataFrame([pop.fitness for pop in population ],columns=columns)
        sort = NSGAII_SORTING(df)
        res = []

        for i,layer in enumerate(sort.layers):
            new_layer = []
            for ind in layer:
                new_ind = Individual(ind)
                new_ind.rank = i + 1
                new_ind.fitness = objectives(ind)
                new_layer.append(new_ind)

            res.append(new_layer)
        return res

   

    def crowding_distance_assignment(self, solutions):

        if len(solutions) == 0:
            return
        for solution in solutions:
            solution.crowding_distance = 0

        for i in range(self.n_objectives):
            solutions.sort(key=lambda solution: solution.fitness[i])

        solutions[0].crowding_distance = solutions[-1].crowding_distance = float('inf')

        fmax = max([[k for k in solution.fitness] for solution in solutions])
        fmin = min([[k for k in solution.fitness] for solution in solutions])

        for i in range(1, len(solutions) - 1):
            for j in range(self.n_objectives):
                solutions[i].crowding_distance += (solutions[i + 1].fitness[j] - solutions[i - 1].fitness[j]) / (fmax[j]-fmin[j])
                


    def run(self, objectives):
        pop = self.population_generator.generate(self.config.n_pop, self.encoding)
        self.n_objectives = len(objectives(pop[0].value))

        fronts = []

        for c in range(self.config.n_iter):

            
            for ind in pop:
                ind.fitness = objectives(ind.value)


            fronts = self.fast_non_dominated_sort(pop,objectives)
            
            for front in fronts:
                self.crowding_distance_assignment(front)
                

            selected = self.selection.pareto_front_selection(fronts, self.config.n_pop)
            children = []

            selected = self.selection.sort_population(selected)

            for i in range(0, self.config.n_pop, self.crossover.n_parents):
                parents = [selected[j + i] for j in range(self.crossover.n_parents)]
                parents = [parent.value for parent in parents]
                children_result = self.crossover.cross_over(parents, self.encoding.bounds)
                # print(children_result)
                for child in children_result:
                    # mutation
                    self.mutation.mutate(child, self.encoding.bounds)
                    child = Individual(child)
                    # print(child.value)
                    children.append(child)

                    # replace population
            pop = self.population_generator.update(children)
        return fronts
