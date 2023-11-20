from src.domain.penalty.ipenalty import PenaltyInterface
import time

class AveragePenalty(PenaltyInterface):

    def adjust_penalty(self,factor:1):
        self.penalty_factor = factor

    def penalty_function(self,x):

        bounds = self.bounds
        
        penalty = 0.0
        for xi, (lower, upper) in zip(x, bounds):
            if xi < lower:
                penalty += (lower - xi) ** 2
            elif xi > upper:
                penalty += (xi - upper) ** 2


        return self.penalty_factor * penalty

        

    
        
