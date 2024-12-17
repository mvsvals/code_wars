def custom_sort(lst):
    return sorted(lst, key=lambda x: (x[0], -len(x), x))


