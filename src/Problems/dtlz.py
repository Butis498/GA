from pymoo.problems import get_problem
import numpy as np
from .problem import Problem

class Dtlz(Problem):

    def __init__(self,n_dtlz,inverse=False) -> None:
    
        self.n_dtlz = n_dtlz
        self.inverse = inverse
        zs = [[[0.125,0.125,0.25],
                [0.375,0.375,0.25]],
                [[0.5,0.5,1],
                [-1.11022302e-16,0,-5.00000000e-01]],
                [[0.33074772,0.94371921,0.94371921],
                [ 0.16925228,-0.44371921,-0.44371921]],
                [[0.5, 0.5,0.29289322],
                [1.25,1.25,1.45710678]]]

        if inverse:
            self.z = zs[n_dtlz][0]
        else:
            self.z = zs[n_dtlz][1]

        self.name = 'dtlz'+str(n_dtlz)
        problem = get_problem(self.name)
        if self.inverse:
            self.name = 'i'+self.name
        bounds = [(problem.xl[i], problem.xu[i]) for i in range(problem.n_var)]
        n = len(bounds)
        m = len(problem.evaluate(np.random.random(n)))
        self.k = n - m + 1
        super().__init__(n, m,bounds)

    

    @Problem.problem
    def dtlz1(self,x):
        self.g = 100 * (self.k + np.sum((x[self.m-1:] - 0.5)**2 - np.cos(20 * np.pi * (x[self.m-1:] - 0.5))))
        objectives = 0.5 * (1 + self.g) * np.ones(self.m)

        for i in range(self.m):
            for j in range(self.m - (i + 1)):
                objectives[i] *= x[j]
            if i > 0:
                objectives[i] *= 1 - x[self.m - (i + 1)]

        return objectives
    
    @Problem.problem
    def dtlz2(self, x):
        self.g = np.sum((x[self.m-1:] - 0.5)**2)
        objectives = (1 + self.g) * np.ones(self.m)

        for i in range(self.m):
            for j in range(self.m - (i + 1)):
                objectives[i] *= np.cos(x[j] * np.pi / 2)

            if i > 0:
                objectives[i] *= np.sin(x[self.m - (i + 1)] * np.pi / 2)

        return objectives

    @Problem.problem
    def dtlz5(self, x):
        self.g = np.sum((x[self.m-1:] - 0.5)**2)
        theta = np.pi / (4 * (1 + self.g)) * (1 + 2 * self.g * x[:self.m-1])
        objectives = (1 + self.g) * np.ones(self.m)

        for i in range(self.m):
            for j in range(self.m - (i + 1)):
                objectives[i] *= np.cos(theta[j])

            if i > 0:
                objectives[i] *= np.sin(theta[self.m - (i + 1)])

        return objectives

    @Problem.problem
    def dtlz7(self, x):
        self.g = 1 + 9 / self.k * np.sum(x)
        h = self.m - np.sum(x[:self.m-1] / (1.0 + self.g) * (1.0 + np.sin(3.0 * np.pi * x[:self.m-1])))
        objectives = np.concatenate([x[:self.m-1], [1.0 + self.g * h]])

        return objectives


    def _inverse_func(self,x):
        iobjectives = np.zeros(self.m)
        self.inverse = False
        objectives = self.evaluate(x)
        self.inverse = True
        for i in range(len(objectives)):
            iobjectives[i] = 0.5*(1+ self.g) - objectives[i]
        return iobjectives
    
    
    def evaluate(self, x):

        if not self.inverse:
            if self.n_dtlz == 1:
                objectives = self.dtlz1(x)
            elif self.n_dtlz == 2:
                objectives = self.dtlz2(x)
            elif self.n_dtlz == 5:
                objectives = self.dtlz5(x)
            elif self.n_dtlz == 7:
                objectives = self.dtlz7(x)
            else:
                raise ValueError(f"Invalid DTLZ problem number: {self.n_dtlz}")

        else:
            objectives = self._inverse_func(x)

        return objectives


    
