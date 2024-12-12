def high(x):
    highest_word = ['', -1]
    for word in x.split():
        word_value = sum(ord(char) - 96 for char in word)
        if word_value > highest_word[1]:
            highest_word = word, word_value
    return highest_word[0]
