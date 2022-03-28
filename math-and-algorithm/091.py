# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_br

n, x = map(int, input().split())
ans = 0
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        c = x - a - b
        if b < c <= n:
            ans += 1
print(ans)