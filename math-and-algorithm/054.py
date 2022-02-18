# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_at

import numpy as np

MOD = 10 ** 9
n = int(input()) - 1
a = np.matrix([[1, 1], [1, 0]], dtype=np.uint64)
ans = np.identity(2, dtype=np.uint64)
while n > 0:
    if n % 2 != 0:
        ans = ans @ a
        ans %= MOD
    a = a @ a
    a %= MOD
    n >>= 1
print(int(ans[1, 0] + ans[1, 1]) % MOD)
