# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_by

a, b, c = map(int, input().split())
if c == 1:
    print('No')
    exit()
cc = 1
for bb in range(b):
    cc *= c
    if a < cc:
        print('Yes')
        exit()
print('No')