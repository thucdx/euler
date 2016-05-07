import math

# prime sieve
limit = 10 ** 6
sieve = [True for i in range(limit + 1)]
sieve[0] = sieve[1] = False

def is_prime(n):
    if n <= 3:
        return n >= 2
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for i in range(2, limit + 1):
    if sieve[i]:
        j = i * i
        while j <= limit:
            sieve[j] = False
            j += i

t = int(input())
for i in range(t):
    n = int(input())

    if is_prime(n):
        print(n)
        continue

    res = -1
    for j in range(int(math.sqrt(n) + 1), 0, -1):
        if n % j == 0:
            if sieve[j]:
                res = max(res, j)
            k = n // j
            if (k <= limit and sieve[k]) or is_prime(k):
                res = max(res, k)
    if res == -1:
        res = n
    print(res)





