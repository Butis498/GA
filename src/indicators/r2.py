import numpy as np
from scipy.special import comb


def achievement_scalarizing_function(A, W, z, rho=0.0001):

    normalized_diff = [w * (a - z_i) for a, w, z_i in zip(A, W, z)]

    max_diff = max(normalized_diff)

    sum_diff = sum(normalized_diff)

    return max_diff + rho * sum_diff


def simplex_lattice(target, dim):

    def next_combination(combination, H):

        for i in range(dim - 1, -1, -1):
            if combination[i] < H:
                return combination[:i] + [combination[i] + 1] + [0] * (dim - i - 1)
        return None

    H = dim
    while comb(H + dim - 1, dim - 1) < target:
        H += 1

    weight_vectors = []
    current_combination = [0] * dim

    while current_combination:
        if sum(current_combination) == H:
            weight_vectors.append([x / H for x in current_combination])
        current_combination = next_combination(current_combination, H)

    return weight_vectors


'''
this function calculates the r2 indicator for a given set of solutions and a reference point
'''
def r2_indicator(A,z):

    W = simplex_lattice(len(A),len(A[0]))
    unique_vectors = set(tuple(vector) for vector in W)
    cardinality = len(unique_vectors)
    result = 0

    for w in W:
        result +=  np.min([achievement_scalarizing_function(a, w,z) for a in A])

    result *= 1/cardinality
    
    return result
