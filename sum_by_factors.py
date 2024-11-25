# Given a list of integers and a single sum value, return the first two values (parse from the left please)
# in order of appearance that add up to form the sum.
# If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.
# Negative numbers and duplicate numbers can and will appear.
# NOTE: There will also be lists tested of lengths upwards of 10, 000, 000 elements.Be sure your code doesn't time out

def sum_pairs(int_list, int_sum):
    seen_numbers = set()
    for number in int_list:
        remainder = int_sum - number
        if remainder in seen_numbers:
            return [remainder, number]
        seen_numbers.add(number)
