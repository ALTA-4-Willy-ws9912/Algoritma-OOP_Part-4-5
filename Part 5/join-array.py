def join_array_remove_duplicate(arrayA, arrayB):
    combined_array = arrayA + arrayB
    
    from collections import OrderedDict
    unique_elements = list(OrderedDict.fromkeys(combined_array))
    
    return unique_elements


print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))

print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))

print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))