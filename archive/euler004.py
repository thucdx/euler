import bisect


def is_palindrome(n):
    sn = repr(n)
    l = len(sn)
    i, j = 0, l - 1
    while i < j:
        if sn[i] != sn[j]:
            return False
        i, j = i + 1, j - 1
    return True

bank = set()

for i in range(100, 1000):
    for j in range(i, 1000):
        p = i * j
        if is_palindrome(p):
            bank.add(p)

bank = sorted(list(bank))

# print(bank)
t = int(input())
for i in range(t):
    n = int(input())
    pos = bisect.bisect(bank, n - 1)
    print(bank[pos - 1])
