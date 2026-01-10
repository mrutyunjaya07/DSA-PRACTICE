
# Find the second largest number in a list of numbers
def secondLargest(numbers):
    if len(numbers) < 2:
        return None  # Return None if there are less than 2 numbers

    first = second = float('-inf') #initialize to negative infinity
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None # Return None if there is no second largest number 

def secondSmallest(numbers):
    if len(numbers) < 2:
        return None  # Return None if there are less than 2 numbers

    first = second = float('inf') #initialize to positive infinity
    for number in numbers:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number

    return second if second != float('inf') else None # Return None if there is no second smallest number





# Example usage:
numbers = [3, 5, 2, 9, 7]
result = secondLargest(numbers)
print(result)  # Output