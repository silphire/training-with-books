n = int(input())
a = 0
for x in (10000, 5000, 1000):
    a += n // x
    n %= x
print(a)