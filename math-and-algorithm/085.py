n, x, y = map(int, input().split())
for a in range(1, n + 1):
    for b in range(a, n + 1):
        for c in range(b, n + 1):
            d = x - a - b - c
            if a * b * c * d == y:
                print('Yes')
                exit()
print('No')