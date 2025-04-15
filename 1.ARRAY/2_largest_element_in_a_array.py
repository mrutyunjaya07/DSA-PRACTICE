# find the largest element in a array !!


# using max function
def find_largest(arr):

    return max(arr)

arr = [10, 3, 5, 20, 7]



# using loop
def find_largest1(arr):
    max = arr[0]
    n=len(arr)

    for i in range(1,n) :
        if arr[i]>max :
            max = arr[i]
    return max



# using sort function
def find_largest2(arr) :
    arr.sort()

    return arr[n-1]



print(find_largest(arr))  # Output: 20
print(find_largest1(arr))
print(find_largest2(arr))    