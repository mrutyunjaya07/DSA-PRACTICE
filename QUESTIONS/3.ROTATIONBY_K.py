# Rotate an array by k positions to the right!! 
def rotateByK(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than n
    return arr[-k:] + arr[:-k]  # Concatenate the last k elements with the rest of the array




# rotate an array by k positions to the left !!
def rotateByKLeft(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than n
    return arr[k:] + arr[:k]  # Concatenate the elements after k with the first k elements

# Example usage:
array = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_array = rotateByK(array, k)
print(rotated_array)  # Output 

