def ordinalSuffix(number):
    numberStr = str(number)
    lastDigit = numberStr[-1]
    lastTwoDigits = numberStr[-2:]

    if lastTwoDigits == '11' or lastTwoDigits == '12' or lastTwoDigits == '13':
        return numberStr + 'th'
    elif lastDigit == '1':
        return numberStr + 'st'
    elif lastDigit == '2':
        return numberStr + 'nd'
    elif lastDigit == '3':
        return numberStr + 'rd'
    else:
        return numberStr + 'th'
    
# tests
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'