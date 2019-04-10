#link: https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN/solutions?solutionId=D2zrssEW4Zu7xjpZg

def addBorder(m):
    rows = len(m)
    columns = len(m[0])
    result = [""]
    for x in range(rows+1):
        for y in range(columns+2):
            if x == 0 or x == rows+2:
                result[x] += "*"
        result.append("*")
    for x in range(rows):
        for y in range(columns):
            result[x+1] += m[x][y]
    for x in range(rows+1):
        result[x+1] += "*"
    for x in range(columns):
        result[-1] += "*"
    return result