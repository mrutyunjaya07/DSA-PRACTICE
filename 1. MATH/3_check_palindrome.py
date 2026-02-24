# you are given a num ber, you need to check if the number is a palindrome or not.
# A palindrome number is a number that remains the same when reversed.

def is_palindrome(n):
    original_num = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original_num == reversed_num 

number = int(input().strip())
if is_palindrome(number):
    print("Palindrome")
else:    
    print("Not a palindrome")
    
