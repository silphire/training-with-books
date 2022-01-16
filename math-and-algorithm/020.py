# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_t

n = int(input())
aa = list(map(int, input().split()))
ans = 0
for x1 in range(n):
    for x2 in range(x1 + 1, n):
        for x3 in range(x2 + 1, n):
            for x4 in range(x3 + 1, n):
                for x5 in range(x4 + 1, n):
                    a = aa[x1] + aa[x2] + aa[x3] + aa[x4] + aa[x5]
                    if a == 1000:
                        ans += 1
print(ans)