#link: https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

def commonCharacterCount(string1, string2):
    total=0
    setStrings = set(string1) &  set(string2)
    for x in setStrings:
        if string1.count(x) < string2.count(x):
            total += string1.count(x)
        else:
            total += string2.count(x)
    return total