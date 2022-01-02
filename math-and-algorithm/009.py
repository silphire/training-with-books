# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_i
n, s = map(int, input().split())
aa = tuple(map(int, input().split()))

cand = set()
for a in aa:
    nc = set([a])
    for c in cand:
        nc.add(c + a)
    cand = cand | nc
if s in cand:
    print('Yes')
else:
    print('No')