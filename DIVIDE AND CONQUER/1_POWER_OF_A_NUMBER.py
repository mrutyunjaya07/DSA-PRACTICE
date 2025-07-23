# find power of a number !!


#defining the funtion
def powerOfNumber(a,n):

    if n==0:
        return 1    #base case
    
    elif n<1 :
        return 1/powerOfNumber(a,-n)  #handling negative inputes
    
    
    mid = n//2
    b=powerOfNumber(a,mid)


    if n%2==0 :
        return b*b
    else :
        return a*b*b
    
#taking input
base=int(input("Enter the base value : "))
power=int(input("Enter the power value : "))

#function call
value=powerOfNumber(base,power)

print("The value is : ", value)
    
    
    
