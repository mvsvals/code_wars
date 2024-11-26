# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the integers to the left of N is equal
# to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.

def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    return -1

test_string = [1,2,3,4,3,2,1]

print(find_even_index(test_string))