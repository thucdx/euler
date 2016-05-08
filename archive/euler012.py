def generate_sieve_divisor(limit):
    sieve = [i for i in range(limit + 1)]

    for i in range(2, limit + 1):
        if sieve[i] == i:
            j = i * i
            while j <= limit:
                sieve[j] = i
                j += i
    return sieve


def triangle_number(n):
    return n * (n + 1) // 2

MAX_NUM = 10 ** 5
LIMIT = 10**3
sieve = generate_sieve_divisor(MAX_NUM)

# num_divisors[i]: total number of divisor of i, for example: num_divisors[6] = 4 {1,2,3,6}
num_divisors = [0, 1, 2, 2]
for x in range(4, MAX_NUM + 1):
    if sieve[x] == x:
        num_divisors.append(2)
    else:
        y, p, m = x, 1, 0
        while y % sieve[x] == 0:
            y //= sieve[x]
            p *= sieve[x]
            m += 1
        total = m + 1 if y == 1 else num_divisors[p] * num_divisors[y]
        num_divisors.append(total)

# num_divisor_triangle[i]: total number of divisor of i * (i + 1) / 2
num_divisor_triangle = []
for i in range(MAX_NUM):
    if i % 2 == 0:
        total = num_divisors[i // 2] * num_divisors[i + 1]
    else:
        total = num_divisors[i] * num_divisors[(i + 1) // 2]

    num_divisor_triangle.append(total)

# res[i] is the smallest number k such that triangle_number(k) has over i divisors
res = [0 for i in range(LIMIT + 1)]
total_divisor, pos = 0, 0

for i in range(MAX_NUM):
    cur = num_divisor_triangle[i]
    if cur > total_divisor:
        while pos < cur and pos <= LIMIT:
            res[pos] = i
            pos += 1
        total_divisor = cur
    if total_divisor >= LIMIT:
        break

T = int(input())
for i in range(T):
    N = int(input())
    print(triangle_number(res[N]))
