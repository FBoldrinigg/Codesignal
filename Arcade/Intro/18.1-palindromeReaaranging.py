#link: https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

def palindromeRearranging(A):
    count = 0
    j = 0
    B = set(A)
    listA = [0]
    for x in B:
        for y in range(len(A)):
            if A[y] == x:
                listA[j] += 1
        j += 1
        listA.append(0)
    for x in listA:
        if x % 2 != 0:
            count += 1
    return count <= 1