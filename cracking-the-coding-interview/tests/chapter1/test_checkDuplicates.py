import pytest
from chapter1 import checkDuplicates as t

def test_checkDuplicates():
    assert t.checkDuplicates('abc') is True
    assert t.checkDuplicates('aabbcc') is False
    assert t.checkDuplicates('') is True