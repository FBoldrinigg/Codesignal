#link: https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5

def avoidObstacles(inputArray):
    inputArray.sort()
    maxD = 2
    for x in range(len(inputArray)):
        for y in range(len(inputArray)): 
            while inputArray[y] % maxD == 0:
                maxD += 1
    return maxD