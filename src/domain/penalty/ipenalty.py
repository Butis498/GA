from abc import ABCMeta, abstractclassmethod


class PenaltyInterface(metaclass=ABCMeta):

    def __init__(self,penalty_factor=10):
        self.penalty_factor = penalty_factor
        self.constraints = {}
    
    def punish(self,ind,bounds,minimize=True,algorithm=None):
        '''punish individual'''
        self.bounds = bounds
        self.algorithm = algorithm
        
        if minimize:
            return self.penalty(ind)
        else:
            return -self.penalty(ind)

    def is_feasible(self,x):

        for constraint in self.constraints:
            constraint_func = constraint["func"]
            lower_bound = constraint["lower_bound"]
            upper_bound = constraint["upper_bound"]

            constraint_value = constraint_func(x)


            if lower_bound is not None and constraint_value < lower_bound:
                return False  # Solution violates the lower bound of a constraint
            if upper_bound is not None and constraint_value > upper_bound:
                return False  # Solution violates the upper bound of a constraint

        for i,bound in zip(x,self.bounds):
            if i < bound[0] or i > bound[1]:
                return False
        

        return True 

    def penalty(self, x):
        penalty_value = 0

        for constraint in self.constraints:
            constraint_func = constraint["func"]
            lower_bound = constraint["lower_bound"]
            upper_bound = constraint["upper_bound"]
            constraint_value = constraint_func(x)
            
            if lower_bound is not None and constraint_value < lower_bound:
                violation = lower_bound - constraint_value
                penalty_value += self.penalty_factor * self.penalty_function(violation)   
            if upper_bound is not None and constraint_value > upper_bound:
                violation = constraint_value - upper_bound
                penalty_value += self.penalty_factor  * self.penalty_function(violation) 

        return penalty_value
    
    @abstractclassmethod
    def penalty_function(self,violation):
        '''Penalty function'''
        return violation
