def balance(arr1, arr2):
    return sorted([arr1.count(char) for char in arr1]) == sorted([arr2.count(char) for char in arr2])