# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bg

MOD = 10 ** 9 + 7
n = int(input())
aa = tuple(sorted(map(int, input().split())))

ans = 0
f = 1
for a in aa:
    ans += f * a
    ans %= 10 ** 9 + 7
    f *= 2
print(ans)