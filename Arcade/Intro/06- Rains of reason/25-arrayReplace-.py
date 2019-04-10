#link https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for x, y in enumerate(inputArray):
        if y == elemToReplace:
            inputArray[x] = substitutionElem
    return inputArray
