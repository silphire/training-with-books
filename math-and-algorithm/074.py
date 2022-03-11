# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bh

n = int(input())
aa = list(map(int, input().split()))
ans = 0
for i, a in enumerate(aa):
    ans += a * (2 * i + 1 - n)
print(ans)