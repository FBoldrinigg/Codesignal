#link: https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE

def arrayMaximalAdjacentDifference(inputArray):
    result = []
    for x in range(len(inputArray) - 1 ):
        result.append(max(inputArray[x],inputArray[x+1]) - min(inputArray[x],inputArray[x+1]))
    return max(result)

