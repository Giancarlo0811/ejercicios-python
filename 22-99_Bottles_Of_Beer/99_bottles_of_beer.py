def displayLyrics():
    i = 99
    while i > 0:
        if i == 1:
            print(f'{i} bottle of beer on the wall,\n')
            print(f'{i} bottle of beer,\n')
            print('Take one down,\n')
            print('Pass it around,\n')
            print('No more bottles of beer on the wall!\n')
        else:
            print(f'{i} bottles of beer on the wall,\n')
            print(f'{i} bottles of beer,\n')
            print('Take one down,\n')
            print('Pass it around,\n')
        i -= 1

displayLyrics()