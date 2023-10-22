import numpy as np

def g1(ind):
    res = 5*ind[0] + 5* ind[1] + 5 * ind[2] + 5*ind[3] - 5 * sum([x**2 for x in range(1,5)])- sum([x for x in range(5,14)])
    return res

def g4(ind):

    res = 5.3578547 * ind[3]**2 + 0.8356891*ind[0]*ind[4] + 37.293639* ind[0] - 40792.141
    return res
    

def g5(ind):

    res = 3*ind[0] + 0.000001*ind[0]**3 + 2*ind[1] + 0.000002/(3*ind[1]**3)
    return res

def g6(ind):
    
    res = (ind[0] - 10)**3 + (ind[1]-20)**3
    return res