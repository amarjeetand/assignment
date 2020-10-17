K, M = [int(x) for x in input().split()]
N = []
for _i_ in range(K):
    N.append([int(x) for x in input().split()][1:])
    
from itertools import product
possible_combination = list(product(*N))

def func(nums):
    return sum(x*x for x in nums) % M

print(max(list(map(func, possible_combination))))
