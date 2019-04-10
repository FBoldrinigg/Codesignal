#link: https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def isIPv4Address(inputString):
    result = []
    temp = ""
    if inputString.count(".") != 3:
        return False
    for x in inputString:
        if x == ".":
            if temp == "":
                return False
            result.append(int(temp))
            temp = ""
        elif x.isdigit() == True:
            temp += x
        else:
            return False
    result.append(int(temp))
    return max(result) < 256 and min(result) > -1
            