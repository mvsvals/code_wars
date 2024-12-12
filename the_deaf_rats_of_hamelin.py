def count_deaf_rats(town):
    index, deaf_rats = 0, 0
    while index < len(town) - 1:
        if town[index] == 'O' and town[index+1] == '~':
            if index < town.index('P'):
                deaf_rats += 1
            index += 2
        elif town[index] == '~' and town[index+1] == 'O':
            if index > town.index('P'):
                deaf_rats += 1
            index += 2
        else:
            index += 1
    return deaf_rats