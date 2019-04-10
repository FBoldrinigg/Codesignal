#link: https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

def isLucky(n):
    digits = [int(x) for x in str(n)]
    half = 0
    firstHalf = 0
    secondHalf = 0
    if len(digits) % 2 == 0:
        half = len(digits) // 2
        for x in range(len(digits)):
            if x < half:
                firstHalf += digits[x]
            else:
                secondHalf += digits[x]
    else:
        half = len(digits) // 2
        for x in range(0, half):
            firstHalf += digits[x]
        for x in range(-half, -1):
            secondHalf += digits[x]
    return firstHalf == secondHalf