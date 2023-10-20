from src.domain.cross_over import CrossOverInterface
from src.domain.mutations import MutationInterface
from src.domain.fitness import FitnessInterface
from src.domain.penalty import PenaltyInterface
from src.domain.encoding import EncodingInterface
from src.domain.selection import SelectionInterface
from src.domain.population import PopulationInterface
from dataclasses import dataclass

@dataclass
class GAConfig():
    n_pop:int = 100
    n_iter:int = 100
    minimize:bool = True


class GeneticAlgorithm(object):

    def __init__(self,cross_over:CrossOverInterface=None,mutation:MutationInterface=None,fitness:FitnessInterface=None,population:PopulationInterface=None,
                 encoding:EncodingInterface=None,penalty:PenaltyInterface=None,selection:SelectionInterface=None,config:GAConfig=None) -> None:
        
        self.crossover = cross_over
        self.mutation = mutation
        self.fitness = fitness
        self.encoding = encoding
        self.penalty = penalty
        self.population_generator = population

        if config:
            self.config = config
        else:
            self.config = GAConfig()


        self.selection = selection

    def __eval(self,score,best,minimize:bool=True):

        if (score < best) and minimize:

            return True
        
        elif (score > best):

            return False
        
        return False
    

    def function_evaluation(self,objective,ind):

        if self.penalty:
            return objective(ind) + self.penalty.punish(ind)
        
        return objective(ind)
            
        

    def run(self,objective,verbose=True):

        
        pop = self.population_generator.generate(self.config.n_pop,self.encoding)
        # keep track of best solution
        best, best_eval = 0, self.function_evaluation(objective,self.encoding.decode(pop[0]))
        # enumerate generations
        for gen in range(self.config.n_iter):
            # self.encoding.decode population
            decoded_ind = [self.encoding.decode(p) for p in pop]
            # evaluate all candidates in the population
            scores = [self.function_evaluation(objective,d) for d in decoded_ind]
            # check for new best solution
            for i in range(self.config.n_pop):
                
                if self.__eval(scores[i],best_eval,self.config.minimize):
                    best, best_eval = pop[i], scores[i]

                    if verbose:
                        print(">%d, new best f(%s) = %f" % (gen,  decoded_ind[i], scores[i]))

            # select parents
            selected = [self.selection.select(pop, scores,self.__eval) for _ in range(self.config.n_pop)]
            # create the next generation
            children = list()
            for i in range(0, self.config.n_pop-1):

                parents = [selected[j+i] for j in range(self.crossover.n_parents)]
                # crossover and mutation
                children_result = self.crossover.cross_over(parents,self.encoding.bounds)

                for child in children_result:
                    # mutation
                    self.mutation.mutate(child)
                    # store for next generation
                    children.append(child)

            # replace population
            pop = self.population_generator.update(children)

        return [best, best_eval]
 


