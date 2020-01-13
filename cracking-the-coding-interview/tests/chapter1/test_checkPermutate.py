import pytest

from chapter1 import checkPermutate as t

def test_checkPermutate():
    assert t.checkPermutate('abc', 'cab') is True
    assert t.checkPermutate('aaa', 'abc') is False
    assert t.checkPermutate('ab', 'abc') is False
    assert t.checkPermutate('', '') is True
    assert t.checkPermutate('aab', 'baa') is True