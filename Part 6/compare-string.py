def compare(A, B):
    lenA = len(A)
    lenB = len(B)
    
    dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
    
    max_length = 0 
    end_index_A = 0 
    
    for i in range(1, lenA + 1):
        for j in range(1, lenB + 1):
            if A[i - 1] == B[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index_A = i 
    
    common_substring = A[end_index_A - max_length: end_index_A]
    return common_substring

# Test cases
print(compare("AKA", "AKASHI"))  # Output: AKA
print(compare("KANGOORO", "KANG"))  # Output: KANG
print(compare("KI", "KIJANG"))  # Output: KI
print(compare("KUPU-KUPU", "KUPU"))  # Output: KUPU
print(compare("ILALANG", "ILA"))  # Output: ILA