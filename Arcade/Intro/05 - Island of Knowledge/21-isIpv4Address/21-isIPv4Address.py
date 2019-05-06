#link: https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def isIPv4Address(inputString):
    if inputString.count(".") != 3 or len(inputString) > 15:
        return False
    inputString = inputString.split(".")
    for x in inputString:
        if not x.isdigit() or not 0 <= int(x) <= 255:
            return False
    return True
            