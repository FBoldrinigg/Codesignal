#link: https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr

def matrixElementsSum(matrix):
    total = 0
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                index = i
                for k in range(index, rows):
                    matrix[k][j] = 0
    for i in range(rows):
        for j in range(columns):
            total += matrix[i][j]
    return total