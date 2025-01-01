def row_sum_odd_numbers(n):
    return sum(n ** 2 - n + 1 + num * 2 for num in range(n))
