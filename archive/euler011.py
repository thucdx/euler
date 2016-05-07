l = 20
a = [list(map(int, input().split())) for i in range(l)]


def is_bound(x, y):
    return 0 <= x < l and 0 <= y < l

d = [[0, 1], [1, 0], [1, 1], [1, -1]]
res = 0
for i in range(l):
    for j in range(l):
        for cur_dir in d:
            p = 1
            for t in range(4):
                nxt_i, nxt_j = i + t * cur_dir[0], j + t * cur_dir[1]
                if is_bound(nxt_i, nxt_j):
                    p *= a[nxt_i][nxt_j]
                else:
                    p = 0
            res = max(res, p)

print(res)
