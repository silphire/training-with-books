import math
h, w = map(int, input().split())
if min(h, w) == 1:
    print(1)
else:
    print(math.ceil(h * w / 2))