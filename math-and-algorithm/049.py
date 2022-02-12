# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ap

n = int(input())
f = [0] * (n + 1)
f[1] = f[2] = 1
for x in range(3, n + 1):
    f[x] = f[x - 1] + f[x - 2]
    f[x] %= 10 ** 9 + 7
print(f[n])