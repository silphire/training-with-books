# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ai

n, q = map(int, input().split())
aa = tuple(map(int, input().split()))
ss = [0] * (n + 1)
for i in range(n):
    ss[i + 1] = ss[i] + aa[i]
for i in range(q):
    l, r = map(int, input().split())
    print(ss[r] - ss[l - 1])