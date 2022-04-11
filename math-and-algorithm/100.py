def multiply(a, b):
    c = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] += a[i][k] * b[k][j]
    return c

q = int(input())
for _ in range(q):
    x, y, z, t = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    t = int(t)

    m = [
        [1 - x, y, 0],
        [0, 1 - y, z],
        [x, 0, 1 - z],
    ]
    mat = None
    while t > 0:
        if t & 1 == 1:
            if mat is None:
                mat = [[m[i][j] for j in range(3)] for i in range(3)]
            else:
                mat = multiply(mat, m)
        m = multiply(m, m)
        t >>= 1
    print(*[sum(mat[i]) for i in range(3)])