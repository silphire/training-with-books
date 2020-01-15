import pytest
from chapter1 import compressChars as t

def test_compressChars():
  assert t.compressChars('') == ''
  assert t.compressChars('a') == 'a'
  assert t.compressChars('abc') == 'abc'
  assert t.compressChars('aabbcc') == 'aabbcc'
  assert t.compressChars('aaabbb') == 'a3b3'
  assert t.compressChars('abbbc') == 'ab3c'
  assert t.compressChars('abcccc') == 'abc4'