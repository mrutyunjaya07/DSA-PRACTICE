# write a program to array by taking input from user .

# Taking input for the size of the array
size = int(input("Size of the array is: ")) 

# Initializing an empty array
arr = []

# Taking input for array elements
for i in range(size):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

# Printing the final array
print(f"The {size}-dimensioned array is: {arr}")


# traversing the array
for i in range(size):
    print(f"The element {i+1} is : {arr[i]} and its index is : {i}")