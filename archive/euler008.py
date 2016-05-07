from functools import reduce
import operator

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    num = list(map(int, list(input())))
    print(max([reduce(operator.mul, num[j:j+k], 1) for j in range(n - k + 1)]))
