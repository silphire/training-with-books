# https://atcoder.jp/contests/math-and-algorithm/tasks/typical90_n

n = int(input())
aa = list(sorted(map(int, input().split())))
bb = list(sorted(map(int, input().split())))
print(sum([abs(aa[i] - bb[i]) for i in range(n)]))