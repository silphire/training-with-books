# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_z

n = int(input())

ans = 0
for x in range(n):
    ans += 1 / (x + 1)
ans *= n
print(ans)