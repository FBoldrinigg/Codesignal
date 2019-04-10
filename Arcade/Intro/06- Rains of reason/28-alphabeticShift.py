#link https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui

def alphabeticShift(inputString):
    abc = list("abcdefghijklmnopqrstuvwxyza")
    result = []
    for x in inputString:
        result.append(abc[abc.index(x) + 1 ])
    result = "".join(result)
    return result