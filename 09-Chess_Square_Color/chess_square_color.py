def getChessSquareColor(column, row):
    if column not in range(0, 7) or row not in range(0, 7):
        return ''
    elif column % 2 == row % 2:
        return 'white'
    else:
        return 'black'
    
# tests
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == ''
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
