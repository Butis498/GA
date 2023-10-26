from src import differential_evolution
from src.repository.cross_over import SinglePointCO
from src.repository.mutation import  PolynomialM
from src.repository.selection import BinaryTS
from src.repository.population import BinaryPopulation
from src.repository.cross_over import SimulatedBC
from src.repository.population import RealP
from src.repository.selection import RandomSelection
from src.repository.encoding import RealEncoding
from src.repository.penalty import AveragePenalty


from src.repository.cross_over import DECrossOver
from src.repository.selection import DESelection
from src.repository.mutation import DEMutation
import numpy as np


mutation = DEMutation(r_mut=0.45)
cross_over = DECrossOver()
population = RealP()
selection = DESelection()
encoding = RealEncoding(bounds=[[-1,3]]*4)
config = differential_evolution.DEConfig(200,150)
penalty = AveragePenalty()

def quadratic_function(x):

    return sum([(xi - 2.0) ** 2 for xi in x])

def objective(x):
    A = 10
    n = len(x)
    return A * n + sum([(xi ** 2 - A * np.cos(2 * np.pi * xi)) for xi in x])


DE = differential_evolution.DifferentialEvolution(cross_over=cross_over,mutation=mutation,population=population,encoding=encoding,selection=selection,config=config,penalty=penalty)
best,best_eval = DE.run(objective=quadratic_function,verbose=True)

print('Best = ',best,' Score = ', best_eval)

