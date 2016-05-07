import math

limit = 3000
res = [-1 for i in range(limit + 1)]

for c in range(1, limit // 2 + 1):
    cc = c * c
    bottom = int(math.sqrt(cc / 2))
    for b in range(bottom, c):
        bb = b * b
        d = cc - bb
        a = int(math.sqrt(d))
        s = a + b + c
        if a * a == d and a < b and s <= limit:
            res[s] = max(res[s], a * b * c)

T = int(input())
for i in range(T):
    N = int(input())
    print(res[N])
