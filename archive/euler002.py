# url: https://www.hackerrank.com/contests/projecteuler/challenges/euler002

limit = 4 * 10 ** 16
fib = [1, 2]
cur, cnt = 0, 2

while cur < limit:
    cur = fib[cnt - 1] + fib[cnt - 2]
    cnt += 1
    fib.append(cur)

t = int(input())
for i in range(t):
    n = int(input())
    total = 0
    j = 0
    while fib[j] <= n:
        if fib[j] % 2 == 0:
            total += fib[j]
        j += 1
    print(total)
