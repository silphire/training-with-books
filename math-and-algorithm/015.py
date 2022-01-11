# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_o

a, b = map(int, input().split())
a, b = max(a, b), min(a, b)
while b > 0:
    if a > b:
        a, b = b, a % b
    else:
        a, b = b % a, a
print(a)