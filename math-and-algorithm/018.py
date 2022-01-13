# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_r

from collections import Counter

n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)

ans = 0
for a, an in sorted(ctr.items()):
    ans += an * ctr[500 - a]
print(ans // 2)