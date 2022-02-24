# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ax

n, x, y = map(int, input().split())

if n % 2 == (abs(x) + abs(y)) % 2:
    if n >= abs(x) + abs(y):
        print('Yes')
    else:
        print('No')
else:
    print('No')