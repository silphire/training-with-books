from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

depth = [120] * (n + 1)
depth[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    nd = depth[x] + 1
    for y in g[x]:
        if depth[y] > nd:
            depth[y] = nd
            q.append(y)

for i in range(n):
    print(depth[i + 1])