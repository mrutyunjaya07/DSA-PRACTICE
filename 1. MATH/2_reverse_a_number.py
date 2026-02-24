# you are given a number, you need to reverse the number and return it.

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

number = int(input().strip("{}[]()"))
print(reverse_number(number))