# sum of all number divisible by k and not greater than N
def get_sum(n, k):
    u = n // k
    return u * (u + 1) // 2 * k

T = int(input())
for i in range(T):
    n = int(input()) - 1
    print(get_sum(n, 3) + get_sum(n, 5) - get_sum(n, 15))
