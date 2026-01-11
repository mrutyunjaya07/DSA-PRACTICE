# Binary Search Implementation (Recursive)


def binarySearch(arr, i, j, key):
    
    if i > j:  # Base condition: If search space is empty
        return -1
    
    mid = (i + j) // 2  # Find the middle index

    # Check if the middle element is the target
    if arr[mid] == key:
        return mid
    
    # If key is greater, search in the right half
    elif arr[mid] < key:
        return binarySearch(arr, mid + 1, j, key)
    
    # If key is smaller, search in the left half
    else:
        return binarySearch(arr, i, mid - 1, key)

# Sorted sample array (Binary Search requires sorted order)
array = [12, 45, 48, 56, 82, 95, 99]

# Defining search space
i = 0
j = len(array) - 1

# Taking user input (ensure it's an integer)
target = int(input("Enter the target: "))

# Call binary search function
index = binarySearch(array, i, j, target)

# Print result
if index == -1:
    print("Not present")
else:
    print("The index is:", index)
