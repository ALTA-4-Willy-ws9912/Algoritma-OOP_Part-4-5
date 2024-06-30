def muncul_sekali(angka):
    frekuensi = {}
    
    for char in angka:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1
    
    hasil = [int(char) for char in frekuensi if frekuensi[char] == 1]
    
    return hasil

# Test cases
print(muncul_sekali("1234123"))  # Output: [4]
print(muncul_sekali("76523752")) # Output: [6, 3]
print(muncul_sekali("12345"))    # Output: [1, 2, 3, 4, 5]
print(muncul_sekali("1122334455")) # Output: []
print(muncul_sekali("0872504"))  # Output: [8, 7, 2, 5, 4]