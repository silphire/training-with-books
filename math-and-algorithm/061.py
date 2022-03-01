# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ba

n = int(input())
x = 1
while x <= n:
    if x == n:
        print('Second')
        exit()
    x = x * 2 + 1
print('First')