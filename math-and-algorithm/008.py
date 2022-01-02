# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_h
n, s = map(int, input().split())
ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a + b <= s:
            ans += 1
print(ans)