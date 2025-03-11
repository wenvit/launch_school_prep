##### Problem statement

# The destinations list contains a list of travel destinations.

# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# Write a function that, without using the built-in in operator, 
# checks whether a specific destination is included within destinations. 
# For example: When checking whether 'Barcelona' is contained in 
# destinations, the expected output is True, 
# whereas the expected output for 'Nashville' is False.

# contains('Barcelona', destinations)  # True
# contains('Nashville', destinations)  # False

##### Solution

# This solution relies on list comprehension to create
# a list of boolean True/False values based on an
# expression using `==` to evaluate whether the given
# city is equal to each element in destinations.
# The `any` keyword is used on the resulting list of boolean values.
# `any` returns True if there's at least one True, else False

def contains(city, lst):

    equality_check = [ city == location 
                      for location in lst ]
    print(any(equality_check))


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

# Launch School solution

# def contains(element, lst):
#     for item in lst:
#         if item == element:
#             return True

#     return False

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False