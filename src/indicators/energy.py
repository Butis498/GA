import numpy as np

def k_s(point1, point2, s):

    distance = np.linalg.norm(np.array(point1) - np.array(point2))
    if s > 0:
        return abs(distance)**-s
    elif s == 0:
        return -np.log(abs(distance))
    else:
        raise ValueError('Incorrrect s value') 


def calculate_s_energy(pareto_front,s=1):
    s_energy = 0
    for i,solution1 in enumerate(pareto_front):
        for j,solution2 in enumerate(pareto_front):
            if i != j:
                distance = np.linalg.norm(np.array(solution1) - np.array(solution2))
                if distance != 0:
                    s_energy += k_s(solution1, solution2,s)
    return s_energy
