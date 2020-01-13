import pytest

from chapter1 import urlify as t

def test_urlify():
    assert t.urlify('') == ''
    assert t.urlify(' ') == '%20'
    assert t.urlify('a b') == 'a%20b'