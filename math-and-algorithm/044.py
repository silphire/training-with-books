# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_an

from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
g = defaultdict(list)
ans = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = deque([1])
ans[1] = 0
while q:
    x = q.popleft()
    for y in g[x]:
        if ans[y] == -1:
            ans[y] = ans[x] + 1
            q.append(y)
for i in range(n):
    print(ans[i + 1])