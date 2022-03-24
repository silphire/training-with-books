# https://atcoder.jp/contests/math-and-algorithm/tasks/arc107_a

MOD = 998244353
a, b, c = map(int, input().split())

# A(A + 1) B(B + 1) C(C + 1) / 8
# ABC(A + 1)(B + 1)(C + 1) / 8
# ABC(ABC + AB + BC + CA + A + B + C + 1) / 8

ab = a * b % MOD
bc = b * c % MOD
ca = c * a % MOD
abc = ab * c % MOD

ans = (abc + ab + bc + ca + a + b + c + 1) % MOD
ans = ans * abc % MOD
ans = ans * pow(8, MOD - 2, MOD) % MOD

print(ans)
