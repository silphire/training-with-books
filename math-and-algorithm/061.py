n = int(input())
x = 1
while x <= n:
    if x == n:
        print('Second')
        exit()
    x = x * 2 + 1
print('First')

# 1 Second
# 2 F
# 3 S
# 4 F
# 5 F
# 6 F
# 7 S
# 8 F
# 9 F
# 10 F
# 11 