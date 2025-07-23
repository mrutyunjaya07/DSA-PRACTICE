# Function definition
def factorial(num):
    # Base case
    if num == 0 :
        return 1
    elif num < 0:
        return "Invalid input !!"
    else:
        return num * factorial(num - 1)  # Recursive function call

# User input
num = int(input("Enter a positive number: "))

# Function call and printing the result
result = factorial(num)
print("Factorial of the number is:", result)
