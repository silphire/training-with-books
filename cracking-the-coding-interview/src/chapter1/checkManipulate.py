# 1.5

def checkManipulate(s: str, t: str) -> bool:
  if abs(len(s) - len(t)) > 1:
    return False

  # find a different point
  i = 0
  while i < len(s) and i < len(t):
    if s[i] != t[i]:
      break
    i += 1
  if len(s) < len(t):
    # append
    s = s[:i] + t[i] + s[i:]
    return s == t
  elif len(s) > len(t):
    # remove
    s = s[:i] + s[i + 1:]
    return s == t
  else:
    # replace
    s = s[:i] + t[i] + s[i + 1:]
    return s == t
