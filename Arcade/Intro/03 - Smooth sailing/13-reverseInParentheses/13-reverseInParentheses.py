#link: https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

def reverseInParentheses(inputString):
    reverse = list(inputString)
    openParentheses = []
    for x, check in enumerate(reverse):
        if check == '(':
            openParentheses.append(x)
        elif check == ')':
            y = openParentheses.pop()
            reverse[y:x] = reverse[x:y:-1]
    for x in range(reverse.count(")")):
        reverse.remove(')')
    return str(''.join(reverse))