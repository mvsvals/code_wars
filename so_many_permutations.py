from itertools import permutations

def find_permutations(s):
    return [''.join(perm) for perm in set(permutations(s))]
