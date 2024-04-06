import random

upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerCase = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
symbol = '~!@#$%^&*()_+'
allChars = upperCase + lowerCase + number + symbol

def generatePassword(length):
    if length < 12:
        length = 12

    password = []
    password.append(upperCase[random.randint(0, 25)])
    password.append(lowerCase[random.randint(0, 25)])
    password.append(number[random.randint(0, 9)])
    password.append(symbol[random.randint(0, 12)])

    while (length > len(password)):
        password.append(allChars[random.randint(0, 74)])

    random.shuffle(password)

    return ''.join(password)

# tests
assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSymbol = False
for character in pw:
    if character in lowerCase:
        hasLowercase = True
    if character in upperCase:
       hasUppercase = True
    if character in number:
        hasNumber = True
    if character in symbol:
        hasSymbol = True
assert hasLowercase and hasUppercase and hasNumber and hasSymbol