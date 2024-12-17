def alphabet_position(text):
    return ' '.join(str(ord(char.lower()) - 96) for char in text if char.isalpha())

# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
print(alphabet_position("The sunset sets at twelve o' clock."))