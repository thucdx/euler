T = int(input())
for i in range(T):
    N = int(input())
    A = [[] for _ in range(N)]
    for j in range(N):
        A[j] = list(map(int, input().split()))

    res = 0
    for k in range(1 << (N - 1)):
        x, y = 0, 0
        total = A[0][0]
        for p in range(N - 1):
            x += 1
            if (k >> p) & 1:
                y += 1
            total += A[x][y]
        res = max(res, total)

    print(res)
