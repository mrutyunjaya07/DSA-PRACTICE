# find minima and maxima from a list

def findMaximaAndMinima(arr,i,j):

    if i ==j:    # base case
        minimum=arr[i]
        maximum=arr[i]

    elif i == j-1: # for two elements
        if arr[i]<arr[j]:
            minimum=arr[i]
            maximum=arr[j]
        else:
            minimum=arr[j]
            maximum=arr[i]

    else:

        mid = i+(j-i)//2

        minl,maxl=findMaximaAndMinima(arr,i,mid)
        minr,maxr=findMaximaAndMinima(arr,mid+1,j)

        if minl<minr:
            minimum=minl
        else:
            minimum=minr
        
        if maxl>maxr:
            maximum=maxl
        else:
            maximum=maxr
    return minimum,maximum

arr=[23,6,98,887,34,0,56,-9]
minimum,maximum=findMaximaAndMinima(arr,0,len(arr)-1)
print("Minimum valuee :",minimum,"Maximum valuee:",maximum)