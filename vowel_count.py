def get_count(sentence):
    return sum(sentence.count(vowel) for vowel in ['a', 'e', 'i', 'o', 'u'])