# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    return [x for x in set(seq) if seq.count(x) % 2 != 0][0]

input_string = [1,2,2,3,3,3,4,3,3,3,2,2,1]
print(find_it(input_string))