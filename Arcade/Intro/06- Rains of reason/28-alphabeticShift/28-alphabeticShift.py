#link https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui

def alphabeticShift(inputString):
    abc = "abcdefghijklmnopqrstuvwxyza"
    result = []
    for x in inputString:
        result.append(abc[abc.index(x) + 1 ])
    return "".join(result)