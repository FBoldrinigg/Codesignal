#link: https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R

def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray
