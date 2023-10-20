from src import genetic_algorithm
from src.repository.cross_over import SinglePointCO
from src.repository.mutation import  PolynomialM
from src.repository.selection import BinaryTS
from src.repository.population import BinaryPopulation
from src.repository.cross_over import SimulatedBC
from src.repository.population import RealP
from src.repository.selection import RandomSelection
from src.repository.encoding import RealEncoding
import numpy as np

mutation = PolynomialM()
cross_over = SimulatedBC()
population = RealP()
selection = RandomSelection()
encoding = RealEncoding(bounds=[[-5,5]]*4)
config = genetic_algorithm.GAConfig(200,2000)



def objective(x):
    A = 10
    n = len(x)
    return A * n + sum([(xi ** 2 - A * np.cos(2 * np.pi * xi)) for xi in x])


GA = genetic_algorithm.GeneticAlgorithm(cross_over=cross_over,mutation=mutation,population=population,encoding=encoding,selection=selection,config=config)
best,best_eval = GA.run(objective=objective)

print('Best = ',best,' Score = ', best_eval)