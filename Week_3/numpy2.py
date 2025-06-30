import numpy as np

numbers = [120, 203, 312, 118, 214]

print(f'The mean is {np.mean(numbers)}')

print(f'The median is {np.median(numbers)}')

print(f'The variance is {np.var(numbers)}')

print(f'The Population standard deviation is {np.std(numbers)}')

print(f'The Sample standard deviation is {np.std(numbers, ddof=1)}')