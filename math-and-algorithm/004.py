# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_d
import functools
print(functools.reduce(lambda a, b: a * b, map(int, input().split())))