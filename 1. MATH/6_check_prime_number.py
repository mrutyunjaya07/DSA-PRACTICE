# you are given a number and you have to check whether it is a prime number or not.
# A prime number is a natural number , which has only two factors, 1 and itself.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input().strip())       
if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")
    
