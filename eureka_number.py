def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    return [num for num in range(a, b+1) if sum(digit ** index for index, digit in enumerate(str(num), 1))]
