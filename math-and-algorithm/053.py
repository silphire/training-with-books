# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_as

#  Sn = 4^0 + 4^1 + ... + 4^n
# 4Sn =       4^1 + ... + 4^n + 4^n+1
# (4-1)Sn = 4^n+1 - 4^0
# Sn = 4^(n+1) - 1 / 3

def modinv(a: int, p: int) -> int:
    """ mod pとした時のaの逆元
    """
    b = p
    u = 1
    v = 0
    while b > 0:
        t = a // b

        a -= t * b
        a, b = b, a

        u -= t * v
        u, v = v, u

    u %= p
    if u < 0:
        u += p
    return u

MOD = 10 ** 9 + 7
n = int(input())
ans = pow(4, n + 1, MOD) - 1
if ans == -1:
    ans = MOD - 1
ans *= modinv(4 - 1, MOD)
ans %= MOD
print(ans)