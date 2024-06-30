import math

def prime_number(number):
    if number <= 1:
        return "Bukan Bilangan Prima"
    if number <= 3:
        return "Bilangan Prima"
    if number % 2 == 0 or number % 3 == 0:
        return "Bukan Bilangan Prima" 
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return "Bukan Bilangan Prima"
        i += 6
    
    return "Bilangan Prima"

# Test Cases
print(prime_number(1000000007)) # Output: Bilangan Prima
print(prime_number(1500450271)) # Output: Bilangan Prima
print(prime_number(1000000000)) # Output: Bukan Bilangan Prima
print(prime_number(10000000019)) # Output: Bilangan Prima
print(prime_number(10000000033)) # Output: Bilangan Prima