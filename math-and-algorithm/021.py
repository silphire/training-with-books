# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_u

n, r = map(int, input().split())
aa = [1]
for i in range(n):
    aa = [1] + [aa[x] + aa[x + 1] for x in range(len(aa) - 1)] + [1]
print(aa[r])