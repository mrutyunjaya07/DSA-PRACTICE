given the number n, count the number of digits in n.        

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

number = int(input().strip())
print(count_digits(number))
