def caesar(offset, input_str):
    result = []
    for char in input_str:
        if char == ' ':
            result.append(char)
        else:
            new_char = chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))
            result.append(new_char)
    return ''.join(result)

# Test cases
print(caesar(3, "abc"))  # Output: "def"
print(caesar(2, "alta"))  # Output: "cnvc"
print(caesar(10, "alterraacademy"))  # Output: "kvdobbkkmknowi"
print(caesar(1, "abcdefghijklmnopqrstuvwxyz"))  # Output: "bcdefghijklmnopqrstuvwxyza"
print(caesar(1000, "abcdefghijklmnopqrstuvwxyz"))  # Output: "mnopqrstuvwxyzabcdefghijkl"