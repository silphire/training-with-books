# https://atcoder.jp/contests/math-and-algorithm/tasks/abc172_d

n = int(input())
d = [0] * (n + 1)
for x in range(1, n + 1):
    for y in range(x, n + 1, x):
        d[y] += 1
ans = 0
for i in range(n + 1):
    ans += i * d[i]
print(ans)