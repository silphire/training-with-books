# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_aa
# https://github.com/E869120/math-algorithm-book/blob/main/editorial/chap3-6/prob3-6-3.py

import sys
sys.setrecursionlimit(200001)

def merge_sort(aa, l, r):
    if r - l <= 1:
        return
    c = (l + r) // 2
    merge_sort(aa, l, c)
    merge_sort(aa, c, r)

    p1 = l
    p2 = c
    p = 0
    na = [0] * (r - l)
    while p1 < c or p2 < r:
        if p1 == c:
            na[p] = aa[p2]
            p2 += 1
        elif p2 == r:
            na[p] = aa[p1]
            p1 += 1
        else:
            if aa[p1] < aa[p2]:
                na[p] = aa[p1]
                p1 += 1
            else:
                na[p] = aa[p2]
                p2 += 1
        p += 1
    for p in range(l, r):
        aa[p] = na[p - l]

n = int(input())
aa = list(map(int, input().split()))
merge_sort(aa, 0, n)
print(' '.join(map(str, aa)))
