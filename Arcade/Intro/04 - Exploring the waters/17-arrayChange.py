#link: https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg/

def arrayChange(inputArray):
    result = 0
    for x in range(len(inputArray)-1):
        if inputArray[x] >= inputArray[x+1]:
            result += inputArray[x] - inputArray[x+1] + 1
            inputArray[x+1] += inputArray[x] - inputArray[x+1] + 1
    return result
