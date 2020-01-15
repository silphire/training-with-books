from typing import List

def zerofy(mat: List[List[int]]) -> List[List[int]]:
  r = []
  for y in range(len(mat)):
    s = []
    for x in range(len(mat[0])):
      s.append(mat[y][x])
    r.append(s)

  for y in range(len(mat)):
    for x in range(len(mat[0])):
      if mat[y][x] != 0:
        continue
      for i in range(len(mat[0])):
        r[y][i] = 0
      for i in range(len(mat)):
        r[i][x] = 0
  print(r)
  return r
