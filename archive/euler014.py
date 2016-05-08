import bisect

inc = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654, 655, 667, 703, 871,
       1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655,
       52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353,
       1564063, 1723519, 2298025, 3064033, 3542887, 3732423]

T = int(input())
for i in range(T):
    N = int(input())
    pos = bisect.bisect_right(inc, N)
    print(inc[pos - 1])

# CODE TO GENERATE INC SEQUENCE
# def memoir(f):
#     mem = {}
#
#     def new_f(n):
#         if n not in mem:
#             mem[n] = f(n)
#         return mem[n]
#     return new_f
#
#
# @memoir
# def seq(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return 1 + seq(n // 2)
#     else:
#         return 1 + seq(3 * n + 1)
#
# LIMIT = 5 * 10**6
# res = [0 for i in range(LIMIT + 1)]
# max_len, has_max_len = -1, -1
#
# inc = []
# for i in range(1, LIMIT):
#     l = seq(i)
#     if l >= max_len:
#         inc.append(i)
#         # print(i, ' ', l)
#         has_max_len = i
#         max_len = l
#     res[i] = has_max_len
#
# print(inc)