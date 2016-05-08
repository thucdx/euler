T = int(input())
for i in range(T):
    N = int(input())
    print(sum([int(c) for c in str(pow(2, N))]))