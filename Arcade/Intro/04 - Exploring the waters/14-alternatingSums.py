#link: https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

def alternatingSums(a):
    team1 = 0
    team2 = 0
    for x, y in enumerate(a):
        if x == 0 or x % 2 == 0:
            team1 += y
        else:
            team2 += y
    return team1, team2
        
