# Bubble Sort Implementation


def bubbleSort(arr):
    n = len(arr)  # Get the length of the array

    # Traverse through all elements
    for i in range(n - 1):
        swapped = False  # Track if any swap happens in this pass

        for j in range( n - i - 1):
            if arr[j] > arr[j + 1]: 
                # Swap if the element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that swapping occurred
        
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break  

    return arr

# Sample array (Unsorted)
array = [12, 45, 2, 34, 21, 56, 7, 28, 56]

print("Original Array:", array)  # Show original array
sortedArray = bubbleSort(array)
print("Sorted Array:", sortedArray)  # Show sorted array
