# you are given a number and you have to find out whether it is an armstrong number or not
# An armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.

def is_armstrong(n):
    original_num = n
    num_digits = len(str(n))
    armstrong_sum = 0
    
    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** num_digits
        n //= 10
        
    return original_num == armstrong_sum

number = int(input().strip())
if is_armstrong(number):
    print("Armstrong")      
else:
    print("Not an Armstrong")
    