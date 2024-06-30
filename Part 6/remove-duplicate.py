def remove_duplicates(array):
    if len(array) == 0:
        return 0
    
    unique_index = 1
    
    for j in range(1, len(array)):
        if array[j] != array[unique_index - 1]:
            array[unique_index] = array[j]
            unique_index += 1
    
    return unique_index

# Test cases
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # Output: 4
print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  # Output: 6
print(remove_duplicates([2, 2, 2, 11]))  # Output: 2
print(remove_duplicates([2, 2, 2, 11]))  # Output: 2
print(remove_duplicates([1, 2, 3, 11, 11]))  # Output: 4
