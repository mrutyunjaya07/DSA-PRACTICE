

def missingNumber(arr):
    
    n = len(arr) # Since one number is missing, the length of the array is n
    
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    # arr_sum = sum(arr)  # Sum of elements in the array
    # or we can use: 
    arr_sum = 0
    for num in arr:
        arr_sum += num
    return total_sum - arr_sum  # The missing number is the difference

# Example usage:
array = [3, 0, 1]       
print(missingNumber(array))  # Output: 2