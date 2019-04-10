#link https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

def adjacentElementsProduct(inputArray):
    result = inputArray[0] * inputArray[1]
    for index in range(1, len(inputArray)-1):
        if  result < inputArray[index] * inputArray[index+1]:
            result = inputArray[index] * inputArray[index+1]
    return result
