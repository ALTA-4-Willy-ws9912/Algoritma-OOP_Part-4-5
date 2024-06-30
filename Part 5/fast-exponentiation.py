def pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1 
    
    while n > 0:
        if n % 2 == 1:
            result *= x
        
        n //= 2  
        x *= x 
    
    return result

print(pow(2, 3))    # Output: 8
print(pow(7, 2))    # Output: 49
print(pow(10, 5))   # Output: 100000
print(pow(17, 6))   # Output: 24137569
print(pow(5, 3))    # Output: 125