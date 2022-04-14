import random
for _ in range(100):
    while True:
        xs = [random.random() * 2 - 1 for _ in range(2)]
        if (xs[0] ** 2 + xs[1] ** 2) ** 0.5 <= 1:
            break
    print(f'{xs[0]:.6f} {xs[1]:.6f}')
