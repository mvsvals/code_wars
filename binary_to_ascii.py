def binary_to_string(binary):
    return ''.join(chr(int(binary[x:x+8], 2)) for x in range(0, len(binary), 8))


test_string = '0100100001100101011011000110110001101111'
print(binary_to_string(test_string))