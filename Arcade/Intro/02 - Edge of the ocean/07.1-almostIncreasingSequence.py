def almostIncreasingSequence(sequence):
    if len(sequence) < 3:                                                              #if len < 3 = always true
        return True
    for i in range(len(sequence)-1):
        if sequence[i+1] <= sequence[i]:
            index = i
    if index == 0:                                                                      # if s[0] > s[1] delete s[0]  ('a')
        sequence.pop(index)
    elif sequence[index] > sequence[index+1] and sequence[index+1] > sequence[index-1]: #deletes 'b' in case: 'a' < 'b' and 'b' > 'c' like 3, 5, 4
        sequence.pop(index)
    else:                                                                               #Else delete 'c'
        sequence.pop(index+1)
    for i in range(len(sequence)-1):                                                  #Check if list is strictly increasing after removing a element
        if sequence[i+1] <= sequence[i]:
            return False
    return True