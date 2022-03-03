# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bc

n, k = map(int, input().split())
s = sum(map(lambda x: abs(int(x)), input().split()))
if k == s or k > s and (k - s) % 2 == 0:
    print('Yes')
else:
    print('No')