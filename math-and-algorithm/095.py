# https://atcoder.jp/contests/math-and-algorithm/tasks/typical90_j

n = int(input())
s = [[0], [0]]

for i in range(n):
    c, p = map(int, input().split())
    c -= 1
    s[c].append(s[c][-1] + p)
    s[1 - c].append(s[1 - c][-1])

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    print(*[s[0][r] - s[0][l], s[1][r] - s[1][l]])