MODULO = 10**9 + 7


def product(start, end, modulo=MODULO):
    res = 1
    for x in range(start, end + 1):
        res = (res * x) % modulo
    return res

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    # (m+1)*(m+2)*...*(m+n) / n!
    # note that: a/b = a/b * b^(p-1) = a * b^(p-2) [module p] (p is prime and (b,p) =1)
    print(product(M + 1, M + N) * pow(product(1, N), MODULO - 2, MODULO) % MODULO)
