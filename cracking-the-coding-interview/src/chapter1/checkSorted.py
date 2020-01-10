def checkSorted(a, b):
    return sorted(list(a)) == sorted(list(b))

print(checkSorted("abc", "anc"))
print(checkSorted("aabbcc", "abcabc"))