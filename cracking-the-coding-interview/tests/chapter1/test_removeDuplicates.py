import pytest
from chapter1 import removeDuplicates

def test_():
    ls = removeDuplicates.List.generate([1, 2, 3, 2, 4, 3])
    ls.trace()
    print()
    removeDuplicates.removeDuplicates(ls)
    ls.trace()