#link https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq

def absoluteValuesSumMinimization(a):
    median = len(a) // 2
    if len(a) % 2 == 0:
        return a[median - 1]
    return a[median]
    
