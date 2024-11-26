# Once upon a time, on a way through the old wild mountainous west,…
#
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
#
# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

def dir_reduc(arr):
    opposite_pairs = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    index = 0
    while index < len(arr) - 1:
        if opposite_pairs[arr[index]] == arr[index + 1]:
            arr = arr[:index] + arr[index+2:]
            index = max(0, index - 1)
        else:
            index += 1
    return arr
