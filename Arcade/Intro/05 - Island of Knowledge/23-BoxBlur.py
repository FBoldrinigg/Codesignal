#link https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

def boxBlur(image):
    x = len(image) - 2
    y = len(image[0]) - 2
    result = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):         
        for j in range(y):     
            for q in range(3):
                for w in range(3):
                    result[i][j] += image[i+q][j+w] 
            result[i][j] //= 9        
    return result