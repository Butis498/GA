from dataclasses import dataclass
from src.domain.cross_over import CrossOverInterface
from src.domain.mutations import MutationInterface
from src.domain.fitness import FitnessInterface
from src.domain.penalty import PenaltyInterface
from src.domain.encoding import EncodingInterface
from src.domain.selection import SelectionInterface
from src.domain.population import PopulationInterface
import pandas as pd
import numpy as np

@dataclass
class DEConfig():
    n_pop:int = 100
    n_iter:int = 100
    minimize:bool = True

class DifferentialEvolution():

    def __init__(self,cross_over:CrossOverInterface=None,mutation:MutationInterface=None,fitness:FitnessInterface=None,population:PopulationInterface=None,
                 encoding:EncodingInterface=None,penalty:PenaltyInterface=None,selection:SelectionInterface=None,config:DEConfig=None) -> None:
        
        self.crossover = cross_over
        self.mutation = mutation
        self.fitness = fitness
        self.encoding = encoding
        self.penalty = penalty
        self.population_generator = population

        if config:
            self.config = config
        else:
            self.config = DEConfig()


        self.selection = selection

    def __eval(self,score,best):

        if (score < best) and self.config.minimize:

            return True
        
        elif (score > best):

            return False
        
        return False

    def function_evaluation(self,objective,ind):

        if self.penalty :
            #print('Funct eval ============ '+str(objective(ind)) +'  Penalty=========',objective(ind) + self.penalty.punish(ind,self.encoding.bounds,self.config.minimize))
            return objective(ind) + self.penalty.punish(ind,self.encoding.bounds,self.config.minimize,self)
        
        return objective(ind)


    def run(self,objective,verbose=True,report_name=False):

        
        best = 0
    
        
        while isinstance(best, int):

            generation_list = []
            avrg_score_list = []
            best_eval_list = []
            c_out_of_bound_list = []
            pop = self.population_generator.generate(self.config.n_pop,self.encoding)
            # keep track of best solution
            best, best_eval = pop[0], self.function_evaluation(objective,self.encoding.decode(pop[0]))

        
            # enumerate generations
            for gen in range(self.config.n_iter):
                # self.encoding.decode population
                decoded_ind = [self.encoding.decode(p) for p in pop]
                # evaluate all candidates in the population
                scores = [self.function_evaluation(objective,d) for d in decoded_ind]
                scores_function = [objective(x) for x in decoded_ind]     
                scores_penalty = np.array(scores) - np.array(scores_function)
                
               
                # check for new best solution
                out_of_bounds = 0

                for i in range(self.config.n_pop):

                    for item,bound in zip(pop[i],self.encoding.bounds):
                        if item < bound[0] or item > bound[1]:
                            out_of_bounds += 1
                    
                    if self.__eval(scores[i],best_eval):
                        best, best_eval = pop[i], scores[i]

                        if verbose:
                            print(">%d, new best f(%s) = %f" % (gen,  decoded_ind[i], scores[i]))

                decoded_ind = self.selection.stochastic_ranking(decoded_ind,scores_function,scores_penalty)


                generation_list.append(gen)
                avrg_score_list.append(sum(scores) / len(scores))
                best_eval_list.append(best_eval)
                c_out_of_bound_list.append(out_of_bounds)



                     
                children = list()
                # create the next generation
                for i in range(self.config.n_pop):

                    selected = self.selection.select(decoded_ind)
                    u = self.mutation.mutate(selected,self.encoding.bounds)
                    new_ind = self.crossover.cross_over(decoded_ind[i],u)

                    if self.__eval(self.function_evaluation(objective,new_ind),self.function_evaluation(objective,decoded_ind[i])):
                        children.append(new_ind)

                    else:
                        children.append(decoded_ind[i])
                    

                # replace population
                pop = self.population_generator.update(children)

                if report_name != False or report_name == None:
                    report_data = {
                        'generation': generation_list,
                        'avrg_score': avrg_score_list,
                        'best_eval': best_eval_list,
                        'c_out_of_bound': c_out_of_bound_list,
                    }
                    report_df = pd.DataFrame(report_data)
                    report_df.to_csv(str(report_name)+'.csv', index=False)


        return [best, best_eval]