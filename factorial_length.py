import math

def count(n):
    if n == 0 or n == 1:
        return 1
    log_sum = sum(math.log10(i) for i in range(1, n + 1))
    return math.floor(log_sum) + 1

