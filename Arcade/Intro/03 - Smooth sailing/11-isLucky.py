#link: https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

def isLucky(n):
    digits = []
    half = 0
    for x in str(n):
        digits.append(int(x))
    half = len(digits)//2
    firstHalf = sum(digits[:half])
    secondHalf = sum(digits[half:])
    return (firstHalf == secondHalf)