##### Problem statement

# Write a function that checks whether a string is empty or not. 
# For example:

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

##### Solution

# My original approach
# Empty strings are falsy but in this case, want to return True
# if empty so need not operator

# def is_empty(string):

#     return True if not string else False  

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True


# Launch School's more concise solution

# def is_empty(string):

#     return not string

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

# Other Launch School approaches

# def is_empty(string):
#     return string == ''

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

def is_empty(string):
    return len(string) == 0  # this would also work for other collections

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True