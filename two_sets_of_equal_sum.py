def create_two_sets_of_equal_sum(n):
    target = (n * (n + 1) // 2) // 2
    if 1 <= n % 4 <= 2: return []

    output_list = [[], []]
    first_sum = 0
    while n > 0:
        if first_sum + n <= target:
            output_list[0].append(n)
            first_sum += n
        else:
            output_list[1].append(n)
        n -= 1

    return output_list