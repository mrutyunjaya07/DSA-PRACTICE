


# Function definition
def fibonacci(num):
    # Base cases
    if num <= 1:
        return num
    else:
        # Recursive call to generate fibonacci series
        return fibonacci(num - 1) + fibonacci(num - 2)


# Function to print series up to 'num' terms
def fibonacci_series(num):
    series = [fibonacci(i) for i in range(num)]
    return series


# User input
num = int(input("Enter a number: "))

# Printing the Fibonacci series
print("Fibonacci series is:", fibonacci_series(num))
