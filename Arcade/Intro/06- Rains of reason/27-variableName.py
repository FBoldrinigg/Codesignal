#link https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

def variableName(name):
    if name[0].isalpha() == False and name[0] != "_":
        return False
    for x in name:
        if x.isalpha() == False and x.isdigit() == False and x != "_":
            return  False
    return True