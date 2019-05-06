#link https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

def variableName(name):
    if not name[0].isalpha() and name[0] != "_":
        return False
    for x in name:
        if not x.isalpha() and not x.isdigit() and x != "_":
            return  False
    return True