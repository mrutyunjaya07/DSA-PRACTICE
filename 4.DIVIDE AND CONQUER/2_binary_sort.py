def binarySearch(arr, i, j, key):
    if i > j:
        return -1  # Base case: not found

    mid = i + (j - i) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearch(arr, mid + 1, j, key)
    else:
        return binarySearch(arr, i, mid - 1, key)

# Example usage
arr = [2, 13, 24, 38, 45, 57, 89, 105]
key = 13
result = binarySearch(arr, 0, len(arr) - 1, key)

if result != -1:
    print("The position is:", result)
else:
    print("Key not found.")
