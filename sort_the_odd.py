# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
    for index, number in enumerate(source_array):
        if number % 2 != 0:
            source_array[index] = odd_numbers[0]
            odd_numbers.remove(odd_numbers[0])
    return source_array

