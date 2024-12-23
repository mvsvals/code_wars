def remove_smallest(numbers):
    return [] if not numbers else [num for index, num in enumerate(numbers) if index != numbers.index(min(numbers))]
