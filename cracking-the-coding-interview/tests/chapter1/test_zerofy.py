import pytest
from chapter1 import zerofy as t

def test_zerofy():
  expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
  actual = t.zerofy([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
  for y in range(len(expected)):
    for x in range(len(expected[0])):
      assert expected[y][x] == actual[y][x]

  expected = [[0, 0, 0], [0, 1, 1], [0, 1, 1]]
  actual = t.zerofy([[0, 1, 1], [1, 1, 1], [1, 1, 1]])
  for y in range(len(expected)):
    for x in range(len(expected[0])):
      assert expected[y][x] == actual[y][x]

def test_zerofy_allzero():
  expected = [[0, 0], [0, 0]]
  actual = t.zerofy([[0, 0], [0, 0]])
  for y in range(len(expected)):
    for x in range(len(expected[0])):
      assert expected[y][x] == actual[y][x]

def test_zerofy_empty():
  assert t.zerofy([]) == []