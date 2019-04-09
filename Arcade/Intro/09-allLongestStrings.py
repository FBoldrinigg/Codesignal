#link: https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def allLongestStrings(inputArray):
    maxchar = 0
    result = []
    for word in inputArray:
        if maxchar < len(word):
            maxchar = len(word)
    for word in inputArray:
        if len(word) == maxchar:
            result.append(word)
    return result
