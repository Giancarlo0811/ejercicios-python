def printASCIITable():
    for number in range(32, 126 + 1):
        character = chr(number)
        print(f'{number} {character}')

printASCIITable()