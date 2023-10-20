from src.domain.cross_over import CrossOverInterface
import random


class SimulatedBC(CrossOverInterface):

    def cross_over(self,parents,bounds):

        lower_bounds, upper_bounds = zip(*bounds)
        
        offspring = []
        for _ in range(self.n_offspring):
            parent1, parent2 = random.sample(parents, 2)

            child1 = []
            child2 = []

            for p1, p2, lower, upper in zip(parent1, parent2, lower_bounds, upper_bounds):
                if p1 != p2:
                    if random.random() < 0.5:
                        if p1 < p2:
                            beta = 1 + (2.0 * (p1 - p2) / (p2 - p1))
                        else:
                            beta = 1 + (2.0 * (p2 - p1) / (p1 - p2))
                        alpha = 2.0 ** (-(self.r_cross + 1))
                        beta = 1.0 / (beta ** alpha)
                        u = random.random()
                        if u <= 0.5:
                            beta_q = (u * 2.0) ** (1.0 / (self.r_cross + 1))
                        else:
                            beta_q = (1.0 / (2.0 * (1.0 - u))) ** (1.0 / (self.r_cross + 1))
                        c1 = 0.5 * ((p1 + p2) - beta_q * (p2 - p1))
                        c2 = 0.5 * ((p1 + p2) + beta_q * (p2 - p1))
                    else:
                        c1, c2 = p1, p2
                else:
                    c1, c2 = p1, p2
                
                # Clip the values to stay within the specified bounds
                c1 = max(lower, min(upper, c1))
                c2 = max(lower, min(upper, c2))

                child1.append(c1)
                child2.append(c2)

            offspring.append(child1)
            offspring.append(child2)

        return offspring




