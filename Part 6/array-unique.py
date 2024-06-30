def array_unique(arrayA, arrayB):
    setB = set(arrayB)
    
    result = [item for item in arrayA if item not in setB]
    
    return result

# Test cases
print(array_unique([1, 2, 3, 4], [1, 3, 5, 10, 16]))  # Output: [2, 4]
print(array_unique([10, 20, 30, 40], [5, 10, 15, 59]))  # Output: [20, 30, 40]
print(array_unique([1, 3, 7], [1, 3, 5]))  # Output: [7]
print(array_unique([3, 8], [2, 8]))  # Output: [3]
print(array_unique([1, 2, 3], [3, 2, 1]))  # Output: []

