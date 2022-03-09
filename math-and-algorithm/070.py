# https://atcoder.jp/contests/math-and-algorithm/tasks/abc075_d

n, k = map(int, input().split())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())

mins = float('inf')
for x0 in xx:
    for x1 in xx:
        if x0 == x1:
            continue
        for y0 in yy:
            for y1 in yy:
                if y0 == y1:
                    continue
                s = (x1 - x0) * (y1 - y0)
                if s >= mins:
                    continue
                kk = 0
                for p in range(n):
                    if x0 <= xx[p] <= x1 and y0 <= yy[p] <= y1:
                        kk += 1
                        if kk >= k:
                            mins = s
                            break
print(mins)