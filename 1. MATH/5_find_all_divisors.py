# you are given a number and you have to find out its all divisors. 
# A divisor of a number is an integer that can be divided evenly into that number.

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors 

number = int(input().strip())
divisors = find_divisors(number)    
print("Divisors of {}: {}".format(number, divisors))


# optimized version to find divisors of a number

def find_divisors_optimized(n): 
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # To avoid adding the square root twice
                divisors.append(n // i)
    return sorted(divisors)

number = int(input().strip())
divisors = find_divisors_optimized(number)  
print("Divisors of {}: {}".format(number, divisors))
