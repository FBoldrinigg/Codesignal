#link: https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

def sortByHeight(a):
    indexes = []
    totalTrees = 0
    for x in range(len(a)):
        if a[x] == -1:
            indexes.append(x)
            totalTrees += 1
    for x in range(totalTrees):
        a.remove(-1)
    a.sort()
    for x in range(len(indexes)):
        a.insert(indexes[x], -1)
    return a