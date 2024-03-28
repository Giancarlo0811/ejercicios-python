def calculateSum(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    for number in numbers:
        sum += number
    return sum

def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1
    product = 1
    for number in numbers:
        product *= number
    return product

# tests
assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840