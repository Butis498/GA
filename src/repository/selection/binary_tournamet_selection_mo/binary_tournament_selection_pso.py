from src.domain.selection.iselection import SelectionInterface
import random
import functools
import time


class BinaryTSMOPSO(SelectionInterface):


    def select(self, population, minimize=True):


        index1, index2 = random.sample(range(len(population)), 2)
        distance1, distance2 = population[index1].crowding_distance, population[index2].crowding_distance


        if minimize:
            if (population[index1].rank < population[index2].rank) or ((population[index1].rank == population[index2].rank) and (distance1 > distance2)):
                return population[index1]
            return population[index2]
        else:
            if not (population[index1].rank < population[index2].rank) or ((population[index1].rank == population[index2].rank) and (distance1 > distance2)):
                return population[index1]
            return population[index2]
        

    def sort_population(self, population, minimize=True):

        def custom_compare(ind1, ind2):
            if (ind1.rank < ind2.rank) or ((ind1.rank == ind2.rank) and (ind1.crowding_distance > ind2.crowding_distance)):
                return -1
            else :
                return 1
            
        

        key_function = functools.cmp_to_key(custom_compare)

        population.sort(key=key_function)

        return population
    
    
       
        