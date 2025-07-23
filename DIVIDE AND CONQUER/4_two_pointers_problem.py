# finding two numbers whose sum is the target using two pointers

def twoPointers(arr,target):
    l=0
    r=len(arr)-1

    for i in range(r):
        if arr[l] + arr[r] == target:
            return l,r
        elif arr[l] + arr[r] > target:
            r=r-1
        else:
            l=l+1
    return -1,-1

arr=[20,40,45,60,70,90]
target=130
result=twoPointers(arr,target)
print(result)  