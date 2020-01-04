# p.21

buf = []
while True:
    try:
        s = input()
    except EOFError:
        break
    buf.append(s)
for line in reversed(buf):
    print(line)