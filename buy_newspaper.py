def buy_newspaper(s1: str, s2: str) -> int:
    for total_copies in range(1, len(s2) + 1):
        combined_string = s1 * total_copies
        s2_position = 0
        for char in combined_string:
            if s2_position < len(s2) and char == s2[s2_position]:
                s2_position += 1
        if s2_position == len(s2):
            return total_copies
    return -1
