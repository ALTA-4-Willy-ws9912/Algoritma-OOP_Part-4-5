def pair_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1 
        else:
            right -= 1 
    
    return [-1, -1]

# Test cases
print(pair_sum([1, 2, 3, 4, 6], 6)) # Output: [1, 3]
print(pair_sum([2, 5, 9, 11], 11)) # Output: [0, 2]
print(pair_sum([1, 3, 5, 7], 12)) # Output: [2, 3]
print(pair_sum([1, 4, 6, 8], 10)) # Output: [1, 2]
print(pair_sum([1, 5, 6, 7], 6)) # Output: [0, 1]
