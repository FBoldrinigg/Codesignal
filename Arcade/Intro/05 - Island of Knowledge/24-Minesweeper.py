#link https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM

def minesweeper(matrix):
    x = len(matrix)
    y = len(matrix[0])
    A = (0, -1, 1)
    result = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == True:
                for a in A:
                    for b in A:
                        if 0<=i+a<=x-1 and 0<=j+b<=y-1:
                            result[i+a][j+b] += 1
                result[i][j] -= 1
    return result