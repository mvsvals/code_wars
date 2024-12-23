def count(s):
    return {letter: s.count(letter) for letter in set(s)}