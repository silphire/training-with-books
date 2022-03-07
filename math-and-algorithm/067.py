# https://atcoder.jp/contests/math-and-algorithm/tasks/typical90_d

h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]
bb = [[0] * w for _ in range(h)]

for y in range(h):
    s = sum(aa[y])
    for x in range(w):
        bb[y][x] += s
for x in range(w):
    s = sum([aa[y][x] for y in range(h)])
    for y in range(h):
        bb[y][x] += s
for y in range(h):
    for x in range(w):
        bb[y][x] -= aa[y][x]

for y in range(h):
    print(*bb[y])