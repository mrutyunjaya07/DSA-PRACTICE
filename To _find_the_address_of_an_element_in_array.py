#To_find_the_address_of_an_element_in_a_array

import sys

def memoryAddress(arr, i, j, a, b, size):
    # Base address of first element
    baseAddress = id(arr[0][0])  

    # Row-major order calculation
    addressOfElement = baseAddress + ((i * b) + j) * size

    return addressOfElement

# Properly defining a 2D list
arr = [
    [2, 4, 8],
    [90, 53, 15],
    [16, 18, 14]
]

a, b = 3, 3  # Rows and columns

i = int(input("Give i value (row index): "))  # Convert input to integer
j = int(input("Give j value (column index): "))

# Size of an integer in bytes
size = sys.getsizeof(arr[0][0])

# Checking if the indices are valid
if 0 <= i < a and 0 <= j < b:
    address = memoryAddress(arr, i, j, a, b, size)
    print(f"Memory Address of element arr[{i}][{j}] is: {address}")
else:
    print("Invalid index. Please enter values within the array's range.")
