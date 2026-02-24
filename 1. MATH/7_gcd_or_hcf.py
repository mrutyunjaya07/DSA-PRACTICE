# you are given two numbers, you need to find the greatest common divisor (GCD) or highest common factor (HCF) of the two numbers.
# The GCD or HCF of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

def gcd(a, b):
    while a>0 and b>0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a

num1 = int(input().strip())
num2 = int(input().strip())
print("GCD/HCF of {} and {} is: {}".format(num1, num2, gcd(num1, num2)))    