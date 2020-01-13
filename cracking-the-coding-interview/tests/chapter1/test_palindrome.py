# 1.3

import pytest
from chapter1 import palindrome as t

def test_palindrome():
    assert t.palindrome("abcba") is True
    assert t.palindrome("tact coa") is True
    assert t.palindrome("aabbccde") is False
    assert t.palindrome("aaa") is True
    assert t.palindrome("") is True