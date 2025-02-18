# Insertion Sort


def insertionSort(arr):
    n = len(arr)  # length of array
    
    for i in range(1, n):  # Start from the second element (index 1)
        key = arr[i]  # Current element to be inserted in sorted part
        j = i - 1
        
        # Move elements that are greater than key one step ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key
    
    return arr


# Sample array (Unsorted)
array = [12, 45, 2, 34, 21, 56, 7, 28, 56]

print("Original Array:", array)  # Show original array
sortedArray = insertionSort(array)
print("Sorted Array:", sortedArray)  # Show sorted array
