# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_w

n = int(input())
bb = list(map(int, input().split()))
rr = list(map(int, input().split()))

print(sum(bb) / n + sum(rr) / n)