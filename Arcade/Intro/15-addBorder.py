#link: https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN/solutions?solutionId=D2zrssEW4Zu7xjpZg

def addBorder(m):
    rows = len(m)
    columns = len(m[0]) + 2
    result = []
    result.append("*" * columns)
    for x in range(rows):
        result.append("*"+m[x]+"*")
    result.append("*" * columns)
    return result