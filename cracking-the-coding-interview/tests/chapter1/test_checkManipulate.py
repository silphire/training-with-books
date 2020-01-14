import pytest
from chapter1 import checkManipulate as t

def test_checkManipulate():
  assert t.checkManipulate('ab', 'abb') is True
  assert t.checkManipulate('ab', 'abc') is True
  assert t.checkManipulate('abdb', 'abb') is True
  assert t.checkManipulate('bdb', 'db') is True
  assert t.checkManipulate('aad', 'bad') is True
  assert t.checkManipulate('aad', 'aaa') is True
  assert t.checkManipulate('aa', 'bb') is False