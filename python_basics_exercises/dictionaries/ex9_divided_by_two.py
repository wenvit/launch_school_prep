##### Problem statement

# Use a for loop to iterate over the numbers dictionary and 
# return a list containing each number divided by 2 as an 
# integer. The result should be truncated to an integer.
# Assign the returned list to a variable named half_numbers 
# and print its value using print.

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# Expected output

# [50, 25, 12]

##### Solution


numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

# One approach using for loop

# half_numbers = []

# for value in numbers.values():
#     half_numbers.append(value // 2)

# print(half_numbers)


# More concise approach using list comprehension

half_numbers = [ value // 2 for value in numbers.values() ]

print(half_numbers)