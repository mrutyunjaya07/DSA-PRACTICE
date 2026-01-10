def largestNumber(numbers):

    if not numbers: 
        return None  # Return None if the list is empty
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


# Find the smallest number in a list of numbers
def smallestNumber(numbers):

    if not numbers: 
        return None  # Return None if the list is empty
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest