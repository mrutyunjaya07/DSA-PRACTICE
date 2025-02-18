# move zeros to end of an array !!

def moveZeros(arr) :
    nonZero=[]
    for num in arr :
        if num != 0:
            nonZero.append(num)
    return nonZero + [0] * (len(arr)-len(nonZero))


array = [0,12,26,8,0,0,98,7,0,23,34,0,8]
print(moveZeros(array))