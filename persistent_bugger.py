from functools import reduce

def persistence(n):
    total_multiplications = 0
    while n >= 10:
        digits = [int(digit) for digit in str(n)]
        n = reduce(lambda x, y: x * y, digits)
        total_multiplications += 1
    return total_multiplications

