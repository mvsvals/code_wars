def missing_term(first_term, little_chou_sum):
    total_sum, index = 0, 0
    while total_sum <= little_chou_sum:
        total_sum += first_term + index
        index += 1
    return total_sum - little_chou_sum
