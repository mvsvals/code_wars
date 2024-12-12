def disemvowel(string_):
    return ''.join(char for char in string_ if not char.upper() in ['A', 'E', 'I', 'O', 'U'])
