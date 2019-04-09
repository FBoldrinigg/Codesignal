#link: https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def makeArrayConsecutive2(statues):
    statues.sort()
    requiredStatues = 0
    for i in range(len(statues)-1):
        if statues[i+1] - statues[i] > 1:
            requiredStatues += statues[i+1] - statues[i] - 1
    return requiredStatues