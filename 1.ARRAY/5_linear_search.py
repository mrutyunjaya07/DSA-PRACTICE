# Linear search

def linearSearch(arr, key):
    n = len(arr)  
    for i in range(n):
        if arr[i] == key:
            return i  # Return index if key is found
    return -1  # Return -1 only after checking all elements

# Sample list
arr = [12, 36, 15, 8, 0, 44]

# Taking integer input
key = int(input("Target: "))

# Call the function and store the result
index = linearSearch(arr, key)

# Check and print result
if index == -1:
    print("Not present")
else:
    print("Index is", index)
