def compressChars(s: str) -> str:
  if len(s) == 0:
    return s

  t = ''

  n = 1
  i = 1
  cur = s[0]
  while i < len(s):
    if cur == s[i]:
      n += 1
    else:
      t += cur
      if n > 1:
        t += str(n)
      n = 1
      cur = s[i]
    i += 1

  t += cur
  if n > 1:
    t += str(n)

  if len(s) <= len(t):
    return s
  else:
    return t