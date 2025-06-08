# find minima and maxima from a list

#define the funcction
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
        #divide and conquer
        mid = i+(j-i)//2

        #recursive calls
        minl,maxl=findMaximaAndMinima(arr,i,mid)
        minr,maxr=findMaximaAndMinima(arr,mid+1,j)

        #combine
        if minl<minr:
            minimum=minl
        else:
            minimum=minr
        
        if maxl>maxr:
            maximum=maxl
        else:
            maximum=maxr
    return minimum,maximum

#input array
arr=[23,6,98,887,34,0,56,-9]
#function call
minimum,maximum=findMaximaAndMinima(arr,0,len(arr)-1)
#print statement
print("Minimum valuee :",minimum,"Maximum valuee:",maximum)