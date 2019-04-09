#link: https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

def palindromeRearranging(A):
    count = 0
    B = set(A)
    A = list(A)
    for x in B:
            if A.count(x) % 2 != 0:
                count += 1
    return count <= 1
