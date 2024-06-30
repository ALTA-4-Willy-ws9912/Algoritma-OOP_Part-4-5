def find_max_sum_sub_array(k, arr):
    if len(arr) < k:
        return "Array length must be at least 'k'"
    
    max_sum = 0
    current_sum = 0
    
    for i in range(k):
        current_sum += arr[i]
    
    max_sum = current_sum
    
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k] 
        max_sum = max(max_sum, current_sum) 
    
    return max_sum

# Test cases
print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2]))  # Output: 9
print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5]))  # Output: 7
print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1]))  # Output: 5
print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1]))  # Output: 7
print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1]))  # Output: 8
