def delete_nth(order, max_e):
    output_list = []
    for char in order:
        if output_list.count(char) < max_e:
            output_list.append(char)
    return output_list
