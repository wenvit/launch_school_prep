##### Problem statement

# Write a function that returns the first element of a list 
# provided as an argument. For example:

# print(first(['Earth', 'Moon', 'Mars']))  # Earth

# Be sure to handle the case where the input list is empty.

##### Solution


def first(input_list):
     return input_list[0] if input_list else None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # None