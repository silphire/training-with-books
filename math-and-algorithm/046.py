# https://atcoder.jp/contests/math-and-algorithm/tasks/abc007_3

from collections import deque

tb = {'#': -1, '.': float('inf')}
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
cc = [
    list(map(lambda x: tb[x], input().rstrip()))
    for _ in range(r)
]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

q = deque([(sx, sy, 0)])
while q:
    x, y, nf = q.popleft()
    if x == gx and y == gy:
        print(nf)
        exit()
    if not (0 <= x < c and 0 <= y < r):
        continue
    if cc[y][x] <= nf:
        continue
    cc[y][x] = nf
    nf += 1
    q.append((x - 1, y, nf))
    q.append((x + 1, y, nf))
    q.append((x, y - 1, nf))
    q.append((x, y + 1, nf))
