# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_aq

MOD = 10 ** 9 + 7
a, b = map(int, input().split())
ans = 1
while b > 0:
    if b & 1 == 1:
        ans *= a
        ans %= MOD
    a *= a
    a %= MOD
    b >>= 1
print(ans)