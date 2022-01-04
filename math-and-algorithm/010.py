# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_j
n = int(input())
ans = 1
for x in range(2, n + 1):
    ans *= x
print(ans)