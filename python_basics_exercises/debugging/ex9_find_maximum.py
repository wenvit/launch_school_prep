##### Problem statement

# Your colleague has implemented a custom function to find the maximum value 
# in a list. However, the function sometimes works correctly, but other times 
# it produces incorrect results. Can you help your colleague fix the bug?

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = 0
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

#print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
#print(find_maximum([-1, 0, 5, 3]))         # Expected 5
#print(find_maximum([-10, -3, -20, -2]))   # Expected -2


##### Solution

# The find_maximum function works for positive integers but
# it returns 0 when a list containing all negative numbers is 
# passed as the argument. This is because the max_number variable
# is initialized to 0 on line 10, and the `if` statement within the 
# `for` loop only reassigns max_number if number > max_number. 
# With all negative numbers in the list, number is never > max_number.

# Here's one way to fix: initialize the max_number variable by setting it
# to the first value in the list (value at index 0)

def find_maximum(numbers):
    if not numbers:  # guard clause to handle empty lists
        return None
    
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
            
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2