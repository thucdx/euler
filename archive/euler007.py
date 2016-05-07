limit = 10 ** 5 * 2
sieve = [True for i in range(limit + 1)]
sieve[0] = sieve[1] = False

for i in range(2, limit + 1):
    if sieve[i]:
        j = i * i
        while j <= limit:
            sieve[j] = False
            j += i

primes = [i for i in range(limit) if sieve[i]]

t = int(input())
for i in range(t):
    n = int(input())
    print(primes[n - 1])