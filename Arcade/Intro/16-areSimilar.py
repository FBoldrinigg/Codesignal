#link: https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

def areSimilar(a, b):
    count = 0
    for x in range(len(a)):
        if a[x] != b[x]:
            count += 1
    if sorted(a) == sorted(b):
        return count <= 2
    return False