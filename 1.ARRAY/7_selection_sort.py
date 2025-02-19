# Selection Sort


def selectionSort(arr):
    n = len(arr)  # Get the length of the array

    # Traverse through all elements
    for i in range(n):
        min_index = i  # Assume the first element is the minimum

        # Find the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the minimum element index
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Sample array (Unsorted)
array = [12, 45, 2, 34, 21, 56, 7, 28, 56]

print("Original Array:", array)  # Show original array
sortedArray = selectionSort(array)
print("Sorted Array:", sortedArray)  # Show sorted array
