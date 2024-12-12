def dig_pow(n, p):
    total_sum = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))
    return total_sum / n if total_sum % n == 0 else -1
