# move zeros to end of an array !!

def moveZeros(arr) :
    nonZero=[] #initialize an empty list to store non-zero elements
    for num in arr :
        if num != 0:
            nonZero.append(num) #append non-zero elements to the new list
    return nonZero + [0] * (len(arr)-len(nonZero)) #concatenate non-zero elements with the required number of zeros


# Example usage:
array = [0,12,26,8,0,0,98,7,0,23,34,0,8]
print(moveZeros(array))