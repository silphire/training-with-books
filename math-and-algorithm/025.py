# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_y

n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

ans = 0
for a, b in zip(aa, bb):
    ans += a / 3 + b * 2 / 3
print(ans)