# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_s

from collections import Counter
n = int(input())
aa = list(map(int, input().split()))

ans = 0
ctr = Counter(aa)
for _, x in ctr.items():
    ans += x * (x - 1) // 2
print(ans)