def generate_sieve(limit):
    sieve = [True for i in range(limit + 1)]
    sieve[0] = sieve[1] = False

    for i in range(2, limit + 1):
        if sieve[i]:
            j = i * i
            while j <= limit:
                sieve[j] = False
                j += i
    return sieve

limit = 10 ** 6
sieve = generate_sieve(limit)
res = [0 for i in range(limit + 1)]
for i in range(2, limit + 1):
    res[i] = res[i - 1] + i if sieve[i] else res[i - 1]

T = int(input())
for i in range(T):
    N = int(input())
    print(res[N])
