# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_aj

from collections import defaultdict
n, q = map(int, input().split())
d = defaultdict(int)
for _ in range(q):
    l, r, x = map(int, input().split())
    d[l] += x
    d[r + 1] -= x
ans = ''
for i in range(1, n + 1):
    if i == 1:
        continue
    if d[i] > 0:
        ans += '<'
    elif d[i] < 0:
        ans += '>'
    else:
        ans += '='
print(ans)
