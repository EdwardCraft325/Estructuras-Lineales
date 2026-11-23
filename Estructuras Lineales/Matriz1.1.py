m = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

res = [list(row) for row in zip(*m)]
for row in res:
    print(*row)