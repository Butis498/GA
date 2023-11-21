
from src.genetic_algorithm.genetic_alorithm import GeneticAlgorithm
from src.repository.population import Individual
from src.nsga import NSGAII_SORTING
from src.nsga import NSGAII
import pandas as pd
import numpy as np
import random
import math
import time

class NSDEII(NSGAII):
             

    def run(self, objectives):
        pop = self.population_generator.generate(self.config.n_pop, self.encoding)

        self.n_objectives = len(objectives(pop[0].value))
        gen = 0
        fronts = []
        children = []

        while  gen < self.config.n_iter:

            #give a fitness value to each individual
            for ind in pop:
                ind.fitness = objectives(ind.value)

            fronts = self.fast_non_dominated_sort(pop)
            pop = []

            for front in fronts:
                # assigns a crowding distanance to each elemnt in the front
                self.crowding_distance_assignment(front)
                for ind in front:
                    pop.append(ind)

            
            # select the top N indivicuals of the prents + children
            selected = self.selection.sort_population(pop)[:self.config.n_pop]


            selected_front = [ind for ind in selected if ind.rank == 1]


            children = []
            remaining = self.config.n_pop
            for i in range(0, self.config.n_pop):

                

                selected_ind = self.selection.select([individual.value for individual in pop])
                selected_ind[0] = selected_front[random.randint(0,len(selected_front)-1)].value
                u = self.mutation.mutate(selected_ind,self.encoding.bounds)
                new_ind = self.crossover.cross_over(pop[i].value,u)
                    
                lower_bound, upper_bound = [bound[0] for bound in self.encoding.bounds],[bound[1] for bound in self.encoding.bounds]
                new_ind = [max(lb, min(up, y)) for y,lb,up in zip(new_ind,lower_bound,upper_bound)]
                new_ind = Individual(new_ind)

                children.append(new_ind)
                remaining -= 1


                if remaining <= 0:
                    break


                    

            pop = self.population_generator.update(children,selected)

            gen += 1



        return fronts[0][:self.config.n_pop]
