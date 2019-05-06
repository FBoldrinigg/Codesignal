#link: https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr

def matrixElementsSum(matrix):
    total = 0
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(columns):
        for j in range(rows):
            if matrix[j][i] == 0:
                break
            else:
                total += matrix[j][i]
    return total