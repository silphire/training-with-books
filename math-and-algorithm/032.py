# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ad

n, x = map(int, input().split())
aa = list(sorted(map(int, input().split())))

l = 0
r = n
while r - l > 1:
    c = (l + r) // 2
    if aa[c] == x:
        print('Yes')
        exit()
    if aa[c] < x:
        l = c
    else:
        r = c
print('No')