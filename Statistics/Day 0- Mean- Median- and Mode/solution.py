import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))

print('{0}\n{1}\n{2}\n'.format(np.mean(numbers), np.median(numbers), int(stats.mode(numbers)[0])))

