import numpy as np

def utility_function(x, w):
    return np.dot(x, w)

def r2_indicator(A, W):
    unique_vectors = set(tuple(vector) for vector in W)
    cardinality = len(unique_vectors)
    result = 0
    for w in W:
        result +=  np.min([utility_function(a, w) for a in A])

    result *= 1/cardinality
    
    return result
