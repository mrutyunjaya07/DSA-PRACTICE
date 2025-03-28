# Function to count the number of ways to reach the nth Fibonacci number
def countWays(n):
    # Base cases
    if n == 0:
        return 1  # Only one way to stay at 0
    elif n == 1:
        return 1  # Only one way to reach 1

    # Recursive call
    return countWays(n - 1) + countWays(n - 2)


# Taking input from the user
num = int(input("Enter a number: "))

# Function call to count ways
ways = countWays(num)

# Display the result
print(f"Number of ways to reach F({num}) is: {ways}")
