# https://atcoder.jp/contests/math-and-algorithm/tasks/abc186_d

n = int(input())
aa = list(sorted(map(int, input().split())))

ans = 0
cum = 0
for i in range(n):
    ans += aa[i] * i - cum
    cum += aa[i]
print(ans)
