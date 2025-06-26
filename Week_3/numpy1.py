import numpy as np

Results = [23, 34, 26, 38, 32]

print(Results)

print(f'The mean is {np.mean(Results)}')

print(f'The median is {np.median(Results)}')

print(f'The sample standard deviation is {np.std(Results, ddof=1)}')

print(f'The population standard deviation is {np.std(Results)}')

print(f'The variance is {np.var(Results)}')