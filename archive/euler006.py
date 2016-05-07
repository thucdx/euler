def sum_of_square(n):
    return n * (n + 1) // 2 * (2 * n + 1) // 3


def square_of_sum(n):
    return (n * (n + 1) // 2) ** 2

t = int(input())
for i in range(t):
    n = int(input())
    print(square_of_sum(n) - sum_of_square(n))