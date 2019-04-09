#link: https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

def reverseInParentheses(inputString):
    s = list(inputString)
    openParentheses = []
    closedParentheses = 0
    for x, check in enumerate(s):
        if check == '(':
            openParentheses.append(x)
        elif check == ')':
            y = openParentheses.pop()
            s[y:x] = s[x:y:-1]
    for x in s:
        if x == ')':
            closedParentheses += 1
    for x in range(closedParentheses):
        s.remove(')')
    reverseString = ''.join(str(e) for e in s)
    return reverseString