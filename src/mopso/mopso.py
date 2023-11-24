import numpy as np
import matplotlib.pyplot as plt
from src.nsga import NSGAII
from dataclasses import dataclass
from typing import List
import random
import time


@dataclass
class Particle:
    value: List[float]
    fitness: List[float]
    velocity: List[float]
    best_value: List[float]
    best_fitness: List[float]
    crowding_distance:float
    best_crowding_distance:float

@dataclass
class Config:
    n_var:int
    n_iter: int
    n_pop: int
    c1: int
    c2: int
    beta: float
    alpha:float
    w: float
    gamma: float
    n_neighborhoods:int

class MOPSO(NSGAII):

    def __init__(self, encoding, mutation,selection ,config):
        self.config = config
        self.encoding = encoding
        self.mutation = mutation
        self.selection = selection


    def _init_particle(self,objectives):
        
        bounds = self.encoding.bounds
        ind_g = lambda bounds:[random.uniform(l,r) for l,r in bounds]
        value = ind_g(bounds)
        velocity = np.zeros(self.config.n_var)
        cost = objectives(value)
        best_pos = value
        best_cost = cost
        return Particle(value, cost, velocity, best_pos, best_cost, crowding_distance=0.0,best_crowding_distance=0.0)

        
    def maintain_diversity(self, repository, n_neighborhoods, threshold):
        # Divide the repository into n neighborhoods
        neighborhoods = np.array_split(repository, n_neighborhoods)


        new_repository = []
        for neighborhood in neighborhoods:
            crowding_distances = [particle.crowding_distance for particle in neighborhood]

            # Replace infinite values with a large finite number
            crowding_distances = np.where(np.isinf(crowding_distances), np.finfo(np.float64).max, crowding_distances)

            min_crowding_distance = np.min(crowding_distances)
            max_crowding_distance = np.max(crowding_distances)

            # Add a small constant to the denominator to avoid division by zero
            epsilon = 1e-9

            if max_crowding_distance == min_crowding_distance:
                normalized_crowding_distances = np.zeros_like(crowding_distances)
            else:
                normalized_crowding_distances = abs(crowding_distances - min_crowding_distance) / abs(max_crowding_distance - min_crowding_distance + epsilon)
            mean_crowding_distance = np.mean(normalized_crowding_distances)

            if mean_crowding_distance < threshold:
                # If the distance is lower than a threshold then keep the most centered individual of the neighborhood
                most_centered_individual = min(neighborhood, key=lambda particle: abs(particle.crowding_distance - mean_crowding_distance))
                new_repository.append(most_centered_individual)
            else:
                # If the distance is not lower than the threshold, keep all individuals
                new_repository.extend(neighborhood)

        return new_repository




    def copy_particle(self, particle):
        return Particle(
            value=particle.value.copy(),
            fitness=particle.fitness.copy(),
            velocity=particle.velocity.copy(),
            best_value=particle.best_position.copy(),
            best_fitness=particle.best_cost.copy(),
        )

    def dominates(self,x, y):
        x = np.array(x)
        y = np.array(y)
        x_dominate_y = all(x<=y) and any(x<y)
        return x_dominate_y

    def run(self,objectives,verbose=False):

        def find_first_non_inf_element(lst):
            for element in lst:
                if element.crowding_distance != float('inf'):
                    return element


        pop = [self._init_particle(objectives) for _ in range(self.config.n_pop)]
        self.n_objectives = len(objectives(pop[0].value))
        repository = list()
        fronts = self.fast_non_dominated_sort(pop,verbose)
        self.crowding_distance_assignment(fronts[0])
        repository += sorted(fronts[0], key=lambda x: x.crowding_distance)[:self.config.n_pop]

        for _ in range(self.config.n_iter):
            for i in range(self.config.n_pop):

                
                leader = find_first_non_inf_element(repository)
                

                pop[i].velocity = self.config.w*pop[i].velocity \
                + self.config.c1*random.random()* np.subtract(leader.value,pop[i].value)\
                + self.config.c2*random.random()*np.subtract(pop[i].best_value ,pop[i].value)


                pop[i].value = pop[i].value + pop[i].velocity
                for b,y in enumerate(pop[i].value):
                    lower_bound, upper_bound = self.encoding.bounds[b]
                    y = max(lower_bound, min(upper_bound, y))
                    pop[i].value[b] = y


                pop[i].value = self.mutation.mutate(pop[i].value,self.encoding.bounds)

                pop[i].fitness = objectives(pop[i].value)

                if self.dominates(pop[i].fitness, pop[i].best_fitness) and pop[i].crowding_distance > pop[i].best_crowding_distance:
                    pop[i].best_value = pop[i].value
                    pop[i].best_fitness = pop[i].fitness
                    pop[i].best_crowding_distance = pop[i].crowding_distance
                
            repository += self.fast_non_dominated_sort(pop,False)[0]
            repository = self.fast_non_dominated_sort(repository,verbose)[0]
            repository = self.maintain_diversity(repository,self.config.n_neighborhoods,0.5)
            self.crowding_distance_assignment(repository)
            repository = sorted(repository, key=lambda x: x.crowding_distance,reverse=True)[:self.config.n_pop]
            

            
        return repository

