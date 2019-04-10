#link https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9

from itertools import permutations

def countOneDLetter(a, b):
    pair = zip(a, b)
    different = 0
    for (a,b) in pair:
        if a != b:
            different += 1
    if different == 1:
        return 1
    return 0

def stringsRearrangement(a):
    B = permutations(a)
    for x in B:
        results = []
        stringPairs = zip(x, x[1:])
        for (a,b) in stringPairs:
            results.append(countOneDLetter(a,b))
        if all(results):
            return True
    return False
