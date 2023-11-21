from .de_selection import *
import functools

class DESelectionMO(DESelection):



    def sort_population(self, population, minimize=True):

        def custom_compare(ind1, ind2):
            if (ind1.rank < ind2.rank) or ((ind1.rank == ind2.rank) and (ind1.crowding_distance > ind2.crowding_distance)):
                return -1
            else :
                return 1
            
        

        key_function = functools.cmp_to_key(custom_compare)

        population.sort(key=key_function)

        return population
    