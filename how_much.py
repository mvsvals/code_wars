def howmuch(m, n):
    return [[f"M: {money_sum}", f"B: {money_sum // 7}", f"C: {money_sum // 9}"] for money_sum in range(min(m, n), max(m, n) + 1) if money_sum % 9 == 1 and money_sum % 7 == 2]

