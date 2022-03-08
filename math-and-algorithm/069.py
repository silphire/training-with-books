# https://atcoder.jp/contests/math-and-algorithm/tasks/abc178_b

a, b, c, d = map(int, input().split())
print(max(
    a * c,
    a * d,
    b * c,
    b * d,
))