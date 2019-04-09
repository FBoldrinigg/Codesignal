#link: https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

def almostIncreasingSequence(sequence):
    count1 = 0
    count2 = 0
    for x in range(len(sequence) - 1):
        if sequence[x] >= sequence[x+1]:
            count1 += 1
    for x in range(len(sequence)-2):
        if sequence[x] >= sequence[x+2]:
            count2 += 1
    return count1 < 2 and count2 < 2
