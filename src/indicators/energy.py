import numpy as np
import math
def k_s(point1, point2, s):

    distance = np.linalg.norm(np.array(point1) - np.array(point2))
    if s > 0:
        return abs(distance)**-s
    elif s == 0:
        return -np.log(abs(distance))
    else:
        raise ValueError('Incorrrect s value') 


def calculate_s_energy(pareto_front,s=1):
    # Initialize the energy to zero
    energy = 0

    # Iterate over each pair of points
    for i in range(len(pareto_front)):
        for j in range(i + 1, len(pareto_front)):
            distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(pareto_front[i], pareto_front[j])))

            # If the distance is non-zero, contribute to the energy calculation
            if distance > 0:
                energy += 1 / (distance ** s)

    # Return the total calculated energy
    return energy

