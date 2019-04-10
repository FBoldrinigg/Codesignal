#link https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

def shapeArea(n):
    area = [1]
    for index in range (1, n):
        area.append(area[index-1] + index*4)
    return area[n-1]

