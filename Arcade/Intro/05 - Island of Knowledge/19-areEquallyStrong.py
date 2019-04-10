#link: https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and yourLeft + yourRight == friendsLeft + friendsRight