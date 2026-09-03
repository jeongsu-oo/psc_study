R = [[1, 0, 2], [3, 1, 1]]
S = [[4, 1], [2, 5], [0, 3]]


def mm(x, y):
    m = len(x)
    n = len(x[0])
    p = len(y[0])
    c = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            s = 0
            for k in range(n):
                s = s + x[i][k] * y[k][j]
            c[i][j] = s
    return c


print(mm(R, S))
