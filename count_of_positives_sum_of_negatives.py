def count_positives_sum_negatives(arr):
    return [sum(1 for pos_num in arr if pos_num > 0), sum(neg_num for neg_num in arr if neg_num < 0)] if arr else []