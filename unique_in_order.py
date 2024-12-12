def unique_in_order(sequence):
    return [char for index, char in enumerate(sequence) if index == 0 or not char == sequence[index - 1]]