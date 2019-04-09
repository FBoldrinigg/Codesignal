#link: https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

def commonCharacterCount(b1, b2):
    total = 0
    a = 0
    b = 0
    s1 = list(b1)
    s2 = list(b2)
    s1.sort()
    s2.sort()
    if len(s1) == 1:
        for y in range(len(s2)):
            if s1[0] == s2[y]:
                return 1
            else:
                return 0
    if len(s2) == 1:
        for x in range(len(s1)):
            if s1[x] == s2[0]:
                return 1
            else:
                return 0
    for x in s1:
        for y in s2:
            if x == y:
                total += 1
                s2.pop(b)
                s1.pop(a)
            b += 1
        a += 1
        b = 0
    for x in s1:
        for y in s2:
            if x == y:
                total += 1
                s2.pop(b)
            b += 1
        b = 0
    return total