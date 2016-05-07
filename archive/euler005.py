def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return b // gcd(a, b) * a

res = [1]

cur = 1
for i in range(1, 41):
    cur = lcm(cur, i)
    res.append(cur)

t = int(input())

for i in range(t):
    n = int(input())
    print(res[n])
