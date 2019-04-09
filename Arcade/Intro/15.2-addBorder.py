#link: https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

#import numpy  as np
#from numpy import array
"""
def addBorder(m):
    rows = len(m)
    columns = len(m[0])
    new = np.empty((rows+2, columns+2), dtype=str)
    new[:] = "*"
    result = [""]
    n = 0
    for x in range(rows):
        for y in range(columns):
            new[x+1][y+1] = m[x][y]
    y = 0
    for x in array(new).flat:
            result[y] += x
            n += 1
            if n == columns+2:
                y += 1
                result.append("")
                n = 0
    result.pop(-1)    
    return result """