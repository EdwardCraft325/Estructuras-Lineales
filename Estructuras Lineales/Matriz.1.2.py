def fun(m):
    r, c = len(m), len(m[0])
    t = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            t[j][i] = m[i][j]
    return t

m = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]]

res = fun(m)
for row in res:
    print(*row)