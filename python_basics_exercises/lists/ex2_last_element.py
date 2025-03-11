##### Problem statement

# Write a function that returns the last element of a list 
# provided as an argument. For example:

# print(last(['Earth', 'Moon', 'Mars']))  # Mars

# Be sure to handle the case where the input list is empty.

##### Solution

# One approach

# def last(input_list):
#     last_idx = len(input_list) - 1
#     return input_list[last_idx] if input_list else None

# print(last(['Earth', 'Moon', 'Mars']))  # Mars
# print(last([]))     # None

# Launch School solution - simpler

def last(input_list):
    return input_list[-1] if input_list else None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))     # None