def tower_builder(n_floors):
    output_list = []
    for row in range(1, n_floors+1):
        output_list.append(' ' * (n_floors - row) + '*' * (row * 2 - 1) + ' ' * (n_floors - row))
    return output_list