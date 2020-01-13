# 1.4

from collections import Counter

def palindrome(s: str) -> bool:
    s = s.replace(' ', '')
    if len(s) == 0:
        return True
        
    c = Counter(s)
    a = Counter(c.values())
    odds = 0
    evens = 0
    for k, v in a.items():
        if k % 2 == 0:
            evens += v
        else:
            odds += v
    return odds == 0 or odds == 1
