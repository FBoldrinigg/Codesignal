#https://app.codesignal.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW

def evenDigitsOnly(n):
    for x in str(n):
        if int(x) % 2 != 0:
            return False
    return True  
    #return (int(x) %2 == 0 for x in str(n))