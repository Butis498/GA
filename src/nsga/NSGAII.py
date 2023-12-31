
from src.genetic_algorithm.genetic_alorithm import GeneticAlgorithm
from src.repository.population import Individual
from src.nsga import NSGAII_SORTING
import pandas as pd
import numpy as np
import math
import time

class NSGAII(GeneticAlgorithm):

    def fast_non_dominated_sort(self, population,verbose=False):
        sort = NSGAII_SORTING(population)
        if verbose:
            sort.plot_pareto_front_3d(pop=population,n=self.config.n_pop,labels=['f1','f2','f3'])
        return sort.layers
   

    def crowding_distance_assignment(self, solutions):


        if len(solutions) == 0:
            return
        for solution in solutions:
            solution.crowding_distance = 0

        for k in range(self.n_objectives):

            solutions.sort(key=lambda solution: solution.fitness[k],reverse=False)

            solutions[0].crowding_distance = solutions[-1].crowding_distance = float('inf')

            max_value = max([solution.fitness[k] for solution in solutions])
            min_value = min([solution.fitness[k] for solution in solutions])

            if max_value - min_value == 0:
                norm = 10e-10
            else:
                norm = max_value - min_value

            for i in range(1, len(solutions) - 1):

                solutions[i].crowding_distance += solutions[i + 1].fitness[k] - solutions[i - 1].fitness[k]
                
                            


    def run(self, objectives,verbose=False):
        pop = self.population_generator.generate(self.config.n_pop, self.encoding)

        self.n_objectives = len(objectives(pop[0].value))
        gen = 0
        fronts = []
        children = []

        while  gen < self.config.n_iter:

            for ind in pop:
                ind.fitness = objectives(ind.value)

            fronts = self.fast_non_dominated_sort(pop,verbose)
            pop = []

            for front in fronts:
                self.crowding_distance_assignment(front)
                for ind in front:
                    pop.append(ind)

            selected = self.selection.sort_population(pop)[:self.config.n_pop]
            selected = [self.selection.select(selected) for _ in range(self.config.n_pop)]

            children = []

            for i in range(0, self.config.n_pop, self.crossover.n_parents):

                parents = [selected[j + i] for j in range(self.crossover.n_parents)]
                parents = [parent.value for parent in parents]
                children_result = self.crossover.cross_over(parents, self.encoding.bounds)

                for child in children_result:
                    self.mutation.mutate(child, self.encoding.bounds)
                    child = Individual(child)
                    children.append(child)

            pop = self.population_generator.update(children,selected)

            gen += 1
            



        return fronts[0][:self.config.n_pop]
