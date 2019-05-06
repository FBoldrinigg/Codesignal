#link: https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def allLongestStrings(inputArray):
    result = []
    maxchar = max(len(x) for x in inputArray)
    for word in inputArray:
        if len(word) == maxchar:
            result.append(word)
    return result
