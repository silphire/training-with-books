# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_v

from collections import Counter
n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)
ans = 0
for x, c in ctr.items():
    if x == 100000 // 2:
        ans += ctr[x] * (ctr[x] - 1)
    else:
        ans += ctr[x] * ctr[100000 - x]
print(ans // 2)