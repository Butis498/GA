from pymoo.problems import get_problem
import numpy as np

class Problem():

    def __init__(self,n,m,bounds) -> None:
        self.m = m
        self.n = n
        self.bounds = bounds

    def validate_input(self, x):
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        return x
    
    @staticmethod
    def input_validate(func):
        def wrapper(self, x):
            try:
                assert len(x) == self.n
            except AssertionError as e:
                raise AssertionError(str(len(x)) + 'not equal to n =' + str(self.n))
            x = self.validate_input(x)
            return func(self, x)
        return wrapper
    
    @classmethod
    def problem(cls,func):
        @cls.input_validate
        def wrapper(self,x):
            return func(self,x)
        return wrapper


