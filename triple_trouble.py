def triple_double(num1, num2):
    return int(any(digit * 3 in str(num1) and digit * 2 in str(num2) for digit in set(str(num1))))




print(triple_double(666789, 12345667))