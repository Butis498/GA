import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import clear_output


class NSGAII_SORTING(object):
    def __init__(self, population) -> None:
        self.df = pd.DataFrame([pop.fitness for pop in population])
        self.layers = []
        self.df_np = self.df.to_numpy()
        self.population = population.copy()
        self.__sort_dominance()


    def plot_pareto_front_3d(self, pop, n, title="Pareto-optimal Front", labels=None):
        
        fig = plt.figure(figsize=(15, 5))

        # Plot 1: Original View
        ax1 = fig.add_subplot(131, projection='3d')
        x1 = [solution.fitness[0] for solution in pop[:n]]
        y1 = [solution.fitness[1] for solution in pop[:n]]
        z1 = [solution.fitness[2] for solution in pop[:n]]
        ax1.scatter(x1, y1, z1, marker='o', label=f'Front {len(pop)}')
        ax1.set_xlabel(labels[0])
        ax1.set_ylabel(labels[1])
        ax1.set_zlabel(labels[2])
        ax1.set_title(title)
        ax1.legend()

        # Plot 2: Different Angles 1
        ax2 = fig.add_subplot(132, projection='3d')
        x2 = [solution.fitness[0] for solution in pop[:n]]
        y2 = [solution.fitness[1] for solution in pop[:n]]
        z2 = [solution.fitness[2] for solution in pop[:n]]
        ax2.scatter(x2, y2, z2, marker='o', label=f'Front {len(pop)}')
        ax2.set_xlabel(labels[0])
        ax2.set_ylabel(labels[1])
        ax2.set_zlabel(labels[2])
        ax2.set_title(f'{title} - Different Angles 1')
        ax2.legend()
        ax2.view_init(elev=20, azim=30)  # Set custom viewing angles

        # Plot 3: Different Angles 2
        ax3 = fig.add_subplot(133, projection='3d')
        x3 = [solution.fitness[0] for solution in pop[:n]]
        y3 = [solution.fitness[1] for solution in pop[:n]]
        z3 = [solution.fitness[2] for solution in pop[:n]]
        ax3.scatter(x3, y3, z3, marker='o', label=f'Front {len(pop)}')
        ax3.set_xlabel(labels[0])
        ax3.set_ylabel(labels[1])
        ax3.set_zlabel(labels[2])
        ax3.set_title(f'{title} - Different Angles 2')
        ax3.legend()
        ax3.view_init(elev=45, azim=-30)  # Set custom viewing angles
        clear_output(wait=True)
        plt.show()


    
    def plot_pareto_front(self, pop,n, title="Solutions", labels=None):
        fig, ax = plt.subplots()

        x = [solution.fitness[0] for solution in pop[:n]]
        y = [solution.fitness[1] for solution in pop[:n]]

        # Explicitly set the size of markers
        size = 3

        ax.scatter(x, y, s=size, marker='o', label=f'N = {len(x)}')

        ax.set_xlabel(labels[0])
        ax.set_ylabel(labels[1])
        ax.set_title(title)
        ax.legend()

        clear_output(wait=True)
        plt.show()

    def update_record(self):
        self.df = pd.DataFrame([pop.fitness for pop in self.population])
        self.df_np = self.df.to_numpy()
        return self.df_np.copy()
        
    def __sort_dominance(self):
        record = self.df_np.copy()

        while len(record) > 0:
            layer_i = []
            layer_ind = []
            for i in range(len(record)):
                dominated = False
                for j in range(len(record)):
                    if i != j:
                        if all(record[j] <= record[i]) and any(record[j] < record[i]):
                            dominated = True
                            break

                if not dominated:
                    layer_ind.append(self.population[i])
                    layer_i.append(i)

            for ind in layer_ind:
                ind.rank = len(self.layers)+1


            self.population = [ind for i, ind in enumerate(self.population) if i not in layer_i]
            self.layers.append(layer_ind)
            record = self.update_record()

