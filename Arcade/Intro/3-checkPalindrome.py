#link: https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ

def checkPalindrome(inputString):
    A = inputString[::-1]
    if inputString == A:
        return True
    else:
        return False
