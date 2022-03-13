class MOD(object):
    """ mod K 上の演算ライブラリ
    """
    def __init__(self, modulo: int):
        self.modulo = modulo
        self.size = 2
        self.fact = [1, 1]
        self.inv = [1, 1]
        self.finv = [0, 1]
    
    def comb(self, n: int, k: int) -> int:
        """ nCk (組み合わせ) を求める
        """
        if n < k or n < 0 or k < 0:
            return 0
        if n == 0 or k == 0 or n == k:
            return 1
        if self.size < n:
            for i in range(self.size, n + 1):
                self.fact.append(self.fact[-1] * i % self.modulo)
                self.inv.append(self.modulo - self.inv[self.modulo % i] * (self.modulo // i) % self.modulo)
                self.finv.append(self.finv[-1] * self.inv[i] % self.modulo)
            self.size = n
        return self.fact[n] * (self.finv[k] * self.finv[n - k] % self.modulo) % self.modulo


M = 10 ** 9 + 7

n = int(input())
aa = list(map(int, input().split()))
ans = 0
m = MOD(M)
for i, a in enumerate(aa):
    c = m.comb(n - 1, i)
    ans += c * a
    ans %= M
print(ans)